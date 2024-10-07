# # game_level=10
# # enemies=["skeleton","zombie","alien"]

# # def create_enemy():
# #     new_enemy=""
# #     if game_level<5:
# #         new_enemy=enemies[0]

# # print(new_enemy)


# from random import randint
# dice_images=["1","2","3","4","5","6"]
# dice_num=randint(a=1,b=6)
# print(dice_images[dice_num])

#use print
word_per_page=0
pages=int(input("number of pages:"))
word_per_page=int(input("number of word per page:"))
total_word=pages*word_per_page
print(f"pages={pages}")
print(f"word_per_page={word_per_page}")
print(total_word)