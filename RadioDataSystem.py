from  mainRadioDataSystem import RdsConcatenator


# rds.input_rds_text("Hello ")      # Remembers "Hello "
# rds.input_rds_text("darkness, ")  # Remembers "darkness, "
# rds.input_rds_text("my old ")     # Remembers "my old"
# rds.input_rds_text("friend.")     # Remembers "friend."
#
# print(rds.get_text())             # Returns the elements concatenated together
#
# # Returns
# # >>> Hello darkness, my old friend.
# 2
#
# rds.input_rds_text("1 ")
# rds.input_rds_text("2")
# rds.input_rds_text("1 ")    # "1 " is in the list, this means the message has repeated, so list is now ["1 ", "2"]
# rds.input_rds_text("2")     # "2" is the message repeated, so we ignore
#
# print(rds.get_text())
#
# # Returns
# # >>> 1 2
# 3
#
# rds.input_rds_text("cool.")
# rds.input_rds_text("Potatoes ")
# rds.input_rds_text("are ")
#
# print(rds.get_text())
#
# # Returns
# # >>> cool.Potatoes are
# 4
#
# rds.input_rds_text("I love ")
# rds.input_rds_text("spaces ")
# rds.input_rds_text("           ")
# rds.input_rds_text("very much!")
#
# print(rds.get_text())
#
# # Returns
# # >>> I love spaces            very much!
# 5
#
# rds.input_rds_text(" this text won't be returned because the '1 2' has repeated ")
# rds.input_rds_text("1 ")
# rds.input_rds_text("2")
# rds.input_rds_text("1 ")              # "1 " was already there, this means the text is repeating, so the text is what is between the                                         1st "1 " and the 2nd "1 " (including the first, but not the 2nd): ["1 ", "2"]
#
# print(rds.get_text())
#
# # Returns
# # >>> 1 2
# 6
#
# rds.input_rds_text("music ")
# rds.input_rds_text("#1")
# rds.input_rds_text("music ")  # "music " already submitted, create ["music ", "#1"]
#
# print(rds.get_text())
#
# rds.input_rds_text("#1")      # "#1" already in repeated text, do nothing
# rds.input_rds_text("song ")   # !! song not in repeated text, this means a new text started, remembering "song "
# rds.input_rds_text("#2 ")     # remembering "#2"
#
# print(rds.get_text())
#
# # returns
# # >>> music #1
# # >>> song #2
# 7
#
# rds.input_rds_text("Hello ")
# rds.input_rds_text("world!")
# rds.input_rds_text("Hello ")    # Creating "Hello world!" text
# rds.input_rds_text("world!")    # part of repeating text
#
# print(rds.get_text())
#
# rds.input_rds_text("Hello ")    # part of repeating text
# rds.input_rds_text("banana, ")  # !! not part of repeating text, create new text
# rds.input_rds_text("potato")    # remember "potato"
#
# print(rds.get_text())
#
# # returns
# # >>> Hello World!
# # >>> banana, potato