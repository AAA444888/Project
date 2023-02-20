import os
def delete(nid):
    if os.path.exists(nid+".txt"):
        os.remove(str(nid)+".txt")
        print('已刪除檔案')
    else:
        print('找不到檔案')