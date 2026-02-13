import re
from collections import Counter

class SentimentAnalyzer:
    def __init__(self):
        self.positive = {'good','great','excellent','amazing','wonderful','fantastic','love',
                         'happy','joy','perfect','beautiful','awesome','best','brilliant',
                         'superb','outstanding','delightful','pleasant','enjoyable','fabulous'}
        self.negative = {'bad','terrible','awful','horrible','poor','worst','hate','sad',
                         'disappointing','unpleasant','disgusting','pathetic','useless',
                         'annoying','frustrating','boring','dreadful','inferior','nasty'}
        self.stop = {'the','a','an','and','or','but','in','on','at','to','for','of','with',
                     'is','was','are','been','be','have','has','had','do','does','did','will',
                     'would','could','should','may','might','i','you','he','she','it','we',
                     'they','this','that','these'}

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        return [w for w in words if w and len(w) > 2]

    def analyze_sentiment(self, text):
        words = self.clean_text(text)
        poscount = sum(1 for w in words if w in self.positive)
        negcount = sum(1 for w in words if w in self.negative)
        total = len(words)
        if total == 0:
            return "neutral", 0.0, poscount, negcount
        score = (poscount - negcount) / total * 100
        if score > 5:
            sentiment = "positive"
        elif score < -5:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        return sentiment, score, poscount, negcount

    def get_word_frequency(self, text, top_n=15):
        words = self.clean_text(text)
        filtered = [w for w in words if w not in self.stop]
        return Counter(filtered).most_common(top_n)

    def generate_ascii_cloud(self, word_freq, width=60):
        if not word_freq:
            return "No words to display"
        maxf = word_freq[0][1]
        cloud = []
        for w, f in word_freq:
            size = int((f / maxf) * 3) + 1
            if size == 1:
                disp = w
            elif size == 2:
                disp = w.upper()
            else:
                disp = f"**{w.upper()}**"
            cloud.append(disp)
        lines, line, llen = [], [], 0
        for w in cloud:
            wlen = len(w) + 2
            if llen + wlen > width:
                lines.append("  ".join(line))
                line, llen = [w], wlen
            else:
                line.append(w); llen += wlen
        if line:
            lines.append("  ".join(line))
        return "\n".join(lines)

def main():
    analyzer = SentimentAnalyzer()
    print("TEXT SENTIMENT ANALYZER\n" + "="*24)
    print("Enter text (finish with an empty line):")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines).strip()
    if not text:
        print("No text entered. Exiting.")
        return
    sentiment, score, pos, neg = analyzer.analyze_sentiment(text)
    print(f"\nOverall: {sentiment.upper()}  |  Score: {score:.2f}%  |  +:{pos}  -:{neg}\n")
    wf = analyzer.get_word_frequency(text)
    print("WORD CLOUD\n" + "-"*10)
    print(analyzer.generate_ascii_cloud(wf))
    print("\nTOP WORDS")
    for w, f in wf[:10]:
        print(f"{w:12} | {'█'*f} ({f})")

if __name__ == "__main__":
    main()

