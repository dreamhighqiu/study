#coding=utf-8
import yaml
import os
class WriteUserCommand:
	def __init__(self,yamlpath=None):
		if yamlpath == None:
			self.yamlpath = 'userconfig.yaml'
		else:
			self.yamlpath = yamlpath
		#获取文件目录的上一级途径
		self.curPath = os.path.dirname(os.getcwd())

		#获取当前脚本所在文件夹路径
		#self.curPath = os.path.dirname(__file__)

		# 获取yaml文件路径
		self.yamlPath = os.path.join(self.curPath, 'config'+'\\'+self.yamlpath)


	def read_data(self):
		'''
		加载yaml数据

	    '''
		# 获取当前脚本所在文件夹路径

		with open(self.yamlPath,'r') as fr:
			data = yaml.load(fr)
		return data

	def get_value(self,key,port):
		'''
		获取value
		'''
		data = self.read_data()
		value = data[key][port]
		return value

	def write_data(self,i,device,bp,port):
		'''
		写入数据
		'''
		data = self.join_data(i,device,bp,port)
		with open(self.yamlPath,"a") as fr:
			yaml.dump(data,fr)

	def join_data(self,i,device,bp,port):
		data = {
		"user_info_"+str(i):{
		"deviceName":device,
		"bp":bp,
		"port":port
		}
		}
		return data

	def clear_data(self):
		with open(self.yamlPath,"w") as fr:
			fr.truncate()
		fr.close()

	def get_file_lines(self):
		data = self.read_data()
		return len(data)


if __name__ == '__main__':
	write_file = WriteUserCommand()
	print write_file.get_value('user_info_0','deviceName')
    #print write_file.get_value('user_info_0','deviceName')


