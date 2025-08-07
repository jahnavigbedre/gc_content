from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_file = "/content/Ecoli.fna"      # E. coli genome file
window_size = 1000              # Sliding window of 1000 bp
output_csv = "gc_content.csv"

def calculate_gc(seq):
    """Calculate GC content of a DNA sequence."""
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

# Process each sequence in FASTA file
for record in SeqIO.parse(fasta_file, "fasta"):
    sequence = str(record.seq).upper()
    length = len(sequence)

    print("========= GC CONTENT ANALYSIS =========")
    print(f"Genome Name: {record.id}")
    print(f"Genome Length: {length} bp")
    print(f"Window Size: {window_size} bp\n")

    gc_values = []
    positions = []

    for i in range(0, length, window_size):
        window_seq = sequence[i:i+window_size]
        gc = calculate_gc(window_seq)
        gc_values.append(gc)
        positions.append(i)

    # Save to CSV
    with open(output_csv, "w") as out:
        out.write(f"# Genome: {record.id}, Window Size: {window_size} bp\n")
        out.write("Start_Position,GC_Content\n")
        for pos, gc in zip(positions, gc_values):
            out.write(f"{pos},{gc:.2f}\n")

    # Plot
    plt.figure(figsize=(12, 5))
    plt.plot(positions, gc_values, linewidth=1.2, color='green')
    plt.xlabel("Genome Position (bp)")
    plt.ylabel("GC Content (%)")
    plt.title(f"GC Content Across {record.id} (Window = {window_size} bp)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

