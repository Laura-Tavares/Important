# Trimming

### > What it is?
The process of cleaning and processing data in order to remove low-quality reads and adapter sequences.


### > Why is it important?
During the sequencing process, artificially generated *adapter sequences* are added to the ends of the reads. These sequences are used to attach the RNA molecules to the sequencing platform but do not map to regions in the genome. However, if not removed, these adapter sequences can interfere with downstream analysis and lead to inaccurate results. Trimming these sequences from the reads can help to improve the quality of the data.

![image](https://sequencing.qcfail.com/wp-content/uploads/sites/2/2016/02/read_through_adapter.png)

Besides, sequencing data may contain low-quality reads that are caused by sequencing errors, PCR bias, or other factors such as poor sample quality. These reads can also interfere with downstream analysis and lead to inaccurate results. By removing these low-quality reads, researchers can ensure that the data they are analyzing is of high quality and can be used to generate accurate and reliable results.

### > How to do it?
There are different tools available to do the trimming process, such as Trimmomatic and Cutadapt, both are widely used and have good documentation.

#### Example of use:
Here is going to be used **Trim galore** (a wrapper around Cutadapt and FastQC to consistently apply adapter and quality trimming to FastQ files).

That are plenty of params that can be used (that are described on the documentation).

When using *small-RNA sequencing data*, for example, maybe it is interesting to look at reads that have a certain lenght. Here it is being used *-- lenght* to determine the minimum size and *--max_lenght* for the maximum size.

```
trim_galore --length 18  --max_length 35 /path/to/fastq.gz trimmed.fq
```

### > Conclusion
Trimming is an important step in the analysis process. By removing low-quality reads, adapter sequences, and bases that fall below a certain quality threshold, researchers can ensure that the data they are analyzing is of high quality and can be used to generate accurate and reliable results.
