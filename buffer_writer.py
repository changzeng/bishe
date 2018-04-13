# encoding: utf-8
# author: liaochangzeng
# e-mail: 1207338829@qq.com


class BufferWriter(object):
	def __init__(self, file_name, max_buffer_size=10*1024*1024, sep="\n"):
		self.file_name = file_name
		self.sep = sep
		self.fd = open(self.file_name, "w+")
		self.records = []
		self.records_size = 0
		self.max_buffer_size = max_buffer_size

	def update(self, record):
		self.records.append(record)
		self.records_size += len(record)

		if self.records_size >= self.max_buffer_size:
			self.write_to_file()
			self.records = []
			self.records_size = 0

	def update_list(self, _list):
		self.update(self.sep.join(_list))

	def write_to_file(self):
		print("writting to %s" % self.file_name)
		self.fd.write(self.sep.join(self.records))
		self.fd.write(self.sep)

	def close(self):
		if self.records_size > 0:
			self.write_to_file()
		self.fd.close()