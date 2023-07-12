student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
nato= pandas.read_csv("nato_phonetic_alphabet.csv")
#Looping through dictionaries:
nato_dict={}
# for n in student_dict["student"]:
#         for k in n:
#             # for (index,r) in nato.iterrows():
#             #     if k.upper()==r.letter:
#             #         print(r.code)
#             nato_dict={k:r.code for (index,r) in nato.iterrows()  if r.letter==k.upper()}
#             print(nato_dict)



c=input("Enter a word to be deciphered:")
for k in c:
    n = {k: r.code for (index, r) in nato.iterrows() if r.letter == k.upper()}
    for i in n:
        # nato_dict[i]=n[i]
        print(n[i],end=" ")

# for k in nato_dict:
#     print(nato_dict[k], end=" ")





#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

