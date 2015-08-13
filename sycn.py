import csv
import string
import re
import os
import math
import glob
import datetime

#parsing summarize label get proper annotator's name 

for files in glob.glob("*.txt"):
	file_name = files.split(".")[0]
	if "_summarized label" in file_name:

		write_to = file_name.split("_")[0] + "_syncd.txt"
		ofile3=open(write_to,"wb")
		#write_to = "main_annotator.txt"
		#ofile1=open(write_to,"wb")

		clip_num = 1;
		with open(files) as f:
			for line in f:
				words = line.split(" ")
				#ofile1.write(words[3].split("\n")[0] + "\t" + words[2]+"\n")
				#go find rapport rating & confidence of each selected annotator
				os.chdir("/Users/Vivi/Documents/python/annotation")
				for annotation_file in glob.glob("*.txt"):
					annotation_file_name = annotation_file.split(".")[0]
					annotator = words[3].split("\n")[0]
					if annotator in annotation_file_name:
						with open(annotation_file) as af:
							for line in af:
								af_words = line.split("\t")
								start_date = af_words[1].split("@")[0]
								end_date = af_words[2].split("@")[0]
								start_time = af_words[1].split("@")[1]
								end_time = af_words[2].split("@")[1]
								#print start_time + " "+ end_time
								if str(clip_num)+".mp4" == af_words[0]:
									part1 = words[3].split("\n")[0] + "\t" + words[2]+"\t" + line.split("\n")[0]
									s_year = start_date.split("-")[0]
									s_month = start_date.split("-")[1]
									s_day = start_date.split("-")[2]
									e_year = end_date.split("-")[0]
									e_month = end_date.split("-")[1]
									e_day = end_date.split("-")[2]
									s_hour = start_time.split(":")[0]
									s_min = start_time.split(":")[1]
									s_sec= start_time.split(":")[2].split(".")[0]
									if "." in start_time:
										s_ms = start_time.split(":")[2].split(".")[1]
									else:
										s_ms = "0"
									e_hour = end_time.split(":")[0]
									e_min = end_time.split(":")[1]
									e_sec= end_time.split(":")[2].split(".")[0]
									if "." in end_time:
										e_ms = end_time.split(":")[2].split(".")[1]
									else:
										e_ms = "0"
									#go find eye tracker data recored in each 30 seconds
									os.chdir("/Users/Vivi/Documents/python/eyegaze")
									for eyetracker_file in glob.glob("*.txt"):
										eyetracker_file_name = eyetracker_file.split(".")[0]
										if annotator in eyetracker_file_name:
											with open(eyetracker_file) as ef:
												next(ef)
												for line in ef:
													ef_words = line.split(" ")
													cur_date = ef_words[0]
													cur_time = ef_words[1].split("Fixation")[0]
													c_year = cur_date.split("-")[0]
													c_month = cur_date.split("-")[1]
													c_day = cur_date.split("-")[2]
													c_hour = cur_time.split(":")[0]
													c_min = cur_time.split(":")[1]
													c_sec = cur_time.split(":")[2].split(".")[0]
													if "." in cur_time:
														c_ms = cur_time.split(":")[2].split(".")[1]
													else:
														c_ms = "0"
													#print c_year + " "+ c_month+ " "+ c_day+ " "+ c_hour+ " "+ c_min+ " "+ c_sec+ " "+ c_ms
													min_time = datetime.datetime(int(s_year),int(s_month),int(s_day),int(s_hour),int(s_min),int(s_sec),int(s_ms))
													max_time = datetime.datetime(int(e_year),int(e_month),int(e_day),int(e_hour),int(e_min),int(e_sec),int(e_ms))
													_time = datetime.datetime(int(c_year),int(c_month),int(c_day),int(c_hour),int(c_min),int(c_sec),int(c_ms))
													if _time <= max_time and _time >= min_time:
														ofile3.write(part1 +" "+ line)
									clip_num = clip_num + 1
									break





