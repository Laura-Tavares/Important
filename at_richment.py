import pysam
from collections import defaultdict

file_in = "/path/to/bam"

bam = pysam.AlignmentFile(file_in, "rb")
seen = set()

total_reads = 0
ta_rich_reads = 0

for mapping in bam:
	 if not mapping.is_unmapped:
		read_id = mapping.query_name
		if read_id not in seen:
			seen.add(read_id)
			total_reads += 1
			sequence = mapping.query_sequence
			ta_count = sequence.lower().count('t') + sequence.lower().count('a')
			if float(ta_count) / len(sequence) >= 0.8:
				ta_rich_reads += 1

bam.close()

ta_percentage = (float(ta_rich_reads) / total_reads) * 100

print('Total reads: {}'.format(total_reads))
print('Reads A and T rich: {}'.format(ta_rich_reads))
print('Percentage of reads rich with A and T: {:.2f}%'.format(ta_percentage))

