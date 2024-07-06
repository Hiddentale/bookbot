def count_number_of_words(text):
	return len(text)

def count_number_of_characters(text):
	character_count = {}
	for word in text:
		for character in word:
			character = character.lower()
			if character not in character_count:
				character_count[character] = 1
			else:
				character_count[character] += 1
	return character_count

def remove_spaces_from_text(text):
	return text.split()

def sort_on(dict):
	return dict["num"]

def main():
	path_to_file = "books/frankenstein.txt"
	with open(path_to_file) as f:
		file_contents = f.read()
		text_without_spaces = remove_spaces_from_text(file_contents)
		number_of_words = count_number_of_words(text_without_spaces)
		count_number_of_characters(text_without_spaces)
		print(f"--- Begin report of {path_to_file} ---\n")
		print(f"{number_of_words} words found in this document\n")
		dictionary_of_characters = count_number_of_characters(text_without_spaces)
		sorted_dictionary_of_character = sorted(dictionary_of_characters.items(), key=lambda x:x[1], reverse=True)
		for character, count in sorted_dictionary_of_character:
			if character.isalpha():
				print(f"The '{character}' character was found {count} times\n")
		print("--- End report ---")
main()
