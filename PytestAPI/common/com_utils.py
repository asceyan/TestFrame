import os,yaml


class ReadYaml():
    @staticmethod
    def readyaml(yamlpath):
        """
        读取yaml文件内容
        :param yamlpath: yaml文件路径
        :return: yaml文件内容
        """
        if not os.path.isfile(yamlpath):
            raise FileNotFoundError("文件路径不存在，请检查文件路径是否正确 %s"%yamlpath)
        with open (yamlpath, "r", encoding="utf-8")as f:
            content = f.read()
        data = yaml.load(content)   # 将内容转换成字典
        return data


