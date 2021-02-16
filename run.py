import json

def work():
    with open("/pfs/input/datum1.json") as f:
        o = json.load(f)
        with open("/pfs/out/str", "w") as f2:
            f2.write("{}: {}".format(o["name"], o["value"]))
                     
if __name__ == "__main__":
    work()