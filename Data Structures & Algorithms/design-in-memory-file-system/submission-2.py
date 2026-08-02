class File:
    def __init__(self, name: str):
        self.content = None
        self.name = name
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = File("")        

    def ls(self, path: str) -> List[str]:
        current = self.root
        for c in path.split('/'):
            if c == '':
                continue
            if c not in current.children:
                return []
            current = current.children[c]
        if current.content is not None:
            return [current.name]
        return sorted([f.name for f in current.children.values()])

    def mkdir(self, path: str) -> None:
        current = self.root
        for c in path.split('/'):
            if c == '':
                continue
            if c not in current.children:
                current.children[c] = File(c)
            current = current.children[c]

    def addContentToFile(self, filePath: str, content: str) -> None:
        current = self.root
        for c in filePath.split('/'):
            if c == '':
                continue
            if c not in current.children:
                current.children[c] = File(c)
            current = current.children[c]
        if not current.content:
            current.content = content
        else:
            current.content += content

    def readContentFromFile(self, filePath: str) -> str:
        current = self.root
        for c in filePath.split('/'):
            if c == '':
                continue
            if c not in current.children:
                return ""
            current = current.children[c]
        return current.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
