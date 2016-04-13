import itertools

class DNASequence(object):
    DNA = ['G', 'A', 'T', 'C']
    @staticmethod
    def longestDNAsequence(sequence):
        foo = [(k, len(list(g))) for k, g in itertools.groupby(sequence,
            key=lambda x: x in DNASequence.DNA)]

        bar = [i[1] for i in foo if i[0]]
        return max(bar) if len(bar) > 0 else 0

    def otherlongestsequence(self, sequence):
        count = 0
        cmax = 0
        for s in sequence:
            if s in self.DNA:
                count += 1
                cmax = max(count, cmax)
            else:
                count = 0

        return cmax

