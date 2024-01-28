import pandas as pd

# Selects a random sample from vocab and returns a dictionary of it to global scope.
def study_items(input_df, sample_number):
    sampled_df = input_df.sample(n=sample_number)
    return sampled_df

# Ask user to translate Korean vocabulary items. 
def kor_to_eng(input_voc_items):
    
    turns = 0
    correct_answers = 0
    correct_df = pd.DataFrame()
    #incorrect_df = pd.DataFrame()

    while turns < max_voc_items:
    
       for index, row in this_round_vocab.iterrows():
            prompt_value = row['Korean']
            correct_answer = row['English']
            
            user_input = input(f"What is the translation for {prompt_value} in English? ")
            
            if user_input == str(correct_answer):
                print("Correct!")
                #This refactored variable creates a new dataframe with the values to be appended prior to concatenation.
                correct_df = pd.concat([correct_df, pd.DataFrame({'Korean': [prompt_value], 'English': [correct_answer]})], ignore_index=True)
                correct_answers += 1
                turns += 1
            else:
                turns += 1
                print(f"Wrong! The correct answer is {correct_answer}.")
        
       print(f"\nQuiz completed. You got {correct_answers} out of {len(this_round_vocab)} correct.")

# Ask user to translate English vocabulary items.        
def eng_to_kor(input_voc_items):
    
    turns = 0
    correct_answers = 0
    correct_df = pd.DataFrame()
    #incorrect_df = pd.DataFrame()

    while turns < max_voc_items:
    
       for index, row in this_round_vocab.iterrows():
            prompt_value = row['English']
            correct_answer = row['Korean']
            
            user_input = input(f"What is the translation for {prompt_value} in Korean? ")
            
            if user_input == str(correct_answer):
                print("Correct!")
                #This refactored variable creates a new dataframe with the values to be appended prior to concatenation.
                correct_df = pd.concat([correct_df, pd.DataFrame({'Korean': [correct_answer], 'English': [prompt_value]})], ignore_index=True)
                correct_answers += 1
                turns += 1
            else:
                turns += 1
                print(f"Wrong! The correct answer is {correct_answer}.")
        
       print(f"\nQuiz completed. You got {correct_answers} out of {len(this_round_vocab)} correct.")

# Import vocab file - do this every time.
vocab_df = pd.read_excel(r'INSERT FILE PATH HERE')

# Ask user what language they want to translate from.
lang_choice = input('Enter \'k\' to translate from Korean, or \'e\' to translate from English ')

# put if loop in a function. call function.
# At end of each loop, ask if user wants to repeat. If yes, call function again, if not, break.

if lang_choice == 'k':
    # Define max number of vocab items for this round.
    max_voc_items = int(input(f'There are {len(vocab_df)} vocabulary items available. Number of items to study? Enter number: '))
    # Generate dataframe containing study items.
    this_round_vocab = study_items(vocab_df,max_voc_items)
    
    #Error handling.
    if max_voc_items > len(this_round_vocab):
        raise Exception("I don\'t have enough vocabulary items for that.")
    
    kor_to_eng(this_round_vocab)
    
      
elif lang_choice == 'e':
    # Define max number of vocab items for this round.
    max_voc_items = int(input(f'There are {len(vocab_df)} vocabulary items available. Number of items to study? Enter number: '))
    # Generate dataframe containing study items.
    this_round_vocab = study_items(vocab_df,max_voc_items)
    
    #Error handling.
    if max_voc_items > len(this_round_vocab):
        raise Exception("I don\'t have enough vocabulary items for that.")
    
    eng_to_kor(this_round_vocab)
          
else: print('Sorry I don\'t understand that!')