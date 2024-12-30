from compress_pickle import dump
import pandas as pd

# Load your original .pkl file
df = pd.read_pickle("/home/ayush/Documents/AI/Machine_Learning/Projects/RecommendationYourself/Model/similarityScore.pkl")

# Compress and save the .pkl file
compressed_file = "similarity_score_compressed.gz"  # You can choose a different compression extension (e.g., .bz2, .lzma)
dump(df, compressed_file, compression="gzip")

print(f"Compressed file saved as: {compressed_file}")


# from compress_pickle import load
# import pandas as pd

# # Load the compressed file
# compressed_file = "finaldf_compressed.gz"
# df = load(compressed_file, compression="gzip")

# # Save it as a standard .pkl file
# uncompressed_file = "finaldf_uncompressed.pkl"
# df.to_pickle(uncompressed_file)

# print(f"Uncompressed file saved as: {uncompressed_file}")
