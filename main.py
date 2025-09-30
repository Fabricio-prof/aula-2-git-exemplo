import os
import json
import redis

def read_value(r: redis.Redis, key: str, t: str):
    if t == "string":
        return r.get(key)
    if t == "hash":
        return r.hgetall(key)
    if t == "list":
        return r.lrange(key, 0, -1)
    if t == "set":
        return sorted(r.smembers(key))
    if t == "zset":
        return r.zrange(key, 0, -1, withscores=True)
    if t == "stream":
        # pega até 100 eventos por stream (simples)
        return r.xrange(key, min="-", max="+", count=100)
    return f"<tipo {t} não tratado>"

def main():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", "6379"))
    db   = int(os.getenv("REDIS_DB", "0"))
    password = os.getenv("REDIS_PASSWORD")  # se tiver auth

    r = redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)

    dump = {}
    # use SCAN para iterar sem travar o servidor
    for key in r.scan_iter(match="*", count=200):
        t = r.type(key)              # string | hash | list | set | zset | stream | none
        ttl = r.ttl(key)             # -1 = sem TTL, -2 = não existe
        dump[key] = {
            "type": t,
            "ttl": ttl,
            "value": read_value(r, key, t)
        }

    print(json.dumps(dump, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
