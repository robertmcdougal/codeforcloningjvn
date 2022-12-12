# define the original genome
original_genome = "ATAACGT"

# define a list of all possible nucleotides
nucleotides = ['A', 'T', 'C', 'G']

# create an empty list to store the 10 copies of the genome
copies = []

# create a for loop that will iterate 10 times
for i in range(10):
  # create a copy of the original genome
  copy = original_genome

  # choose a random position in the genome to change
  position = random.randint(0, len(original_genome)-1)

  # choose a random nucleotide to change it to
  nucleotide = random.choice(nucleotides)

  # change the nucleotide at the chosen position in the copy
  copy = copy[:position] + nucleotide + copy[position+1:]

  # check if the copy is already in the list of copies
  if copy not in copies:
    # add the copy to the list of copies
    copies.append(copy)

# print the list of copies
print(copies)
