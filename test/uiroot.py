import time
import json

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def get_ui_tree():
    while True:
        ui_tree = poco.agent.hierarchy.dump()
    # navNewInfo = pocouwa.agent.rpc.call("RunCommand", "gm.GetNavInfo()").wait()
    # print(ui_tree,)
    # print(navNewInfo)
    # with open('ui_tree.json',"w+") as f:
    #     f.write(json.dumps(ui_tree, sort_keys=False, indent=2))

# get_ui_tree()

a = [1,2]
b = [2,4]
a.extend(b)
print(a)