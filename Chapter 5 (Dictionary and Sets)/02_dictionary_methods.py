marks = {
    "Riya" : 99,
    "Ram" : 75,
    "Shyam" : 78
}

# print(marks.items())             // Output : dict_items([('Riya', 99), ('Ram', 75), ('Shyam', 78)])
 
# print(marks.keys())               // Output : dict_keys(['Riya', 'Ram', 'Shyam'])

# print(marks.values())               // Output : dict_values([99, 75, 78])

# marks.update({"Riya" : 100})
# print(marks)                           // Output : {'Riya': 100, 'Ram': 75, 'Shyam': 78}

# marks.update({"Riya" : 100, "Priya" : 89})
# print(marks)                    // Output : {'Riya': 100, 'Ram': 75, 'Shyam': 78, 'Priya': 89}

# print(marks.get("Riya"))            # Output : 99
# print(marks["Riya"])                # agr ham normally marks.get aur marks[Riya] wali commands run kre to same output aayega but agr maan lo ham Riya ki jagah aur kuch likhde jo hmari dictionary pe rpesent nhi hai to marks.get wali command output me "None" degi aur dusre wali "Error" degi.
