# 📘 Structured Document Output


## 📄 Page 1 - No Heading Found

- {'id': 'p0', 'text': '• A computational problem specifies an input-output relationship – What does the input look like? – What should the output be for each input? • Example: – Input: an integer number N – Output: Is the number prime? • Example: – Input: A list of names of people – Output: The same list sorted alphabetically • Example: – Input: A picture in digital format – Output: An English description of what the picture shows'}

## 📄 Page 2 - No Heading Found

- {'id': 'p1', 'text': '• An algorithm is an exact specification of how to solve a computational problem • An algorithm must specify every step completely, so a computer can implement it without any further “understanding” • An algorithm must work for all possible inputs of the problem. • Algorithms must be: – Correct: For each input produce an appropriate output – Efficient: run as quickly as possible, and use as little memory as possible – more about this later • There can be many different algorithms for each computational problem.'}

## 📄 Page 3 - No Heading Found

- {'id': 'p2', 'text': '• Algorithms can be implemented in any programming language • Usually we use “pseudo-code” to describe algorithms Testing whether input N is prime: For j = 2 .. N-1 If j|N Output “N is composite” and halt Output “N is prime”'}

## 📄 Page 4 - No Heading Found

- {'id': 'p3', 'text': '• The first algorithm “invented” in history was Euclid’s algorithm for finding the greatest common divisor (GCD) of two natural numbers • Definition: The GCD of two natural numbers x, y is the largest integer j that divides both (without remainder). I.e. j|x, j|y and j is the largest integer with this property. • The GCD Problem: – Input: natural numbers x, y – Output: GCD(x,y) – their GCD'}

## 📄 Page 5 - No Heading Found

- {'id': 'p4', 'text': 'public static int gcd(int x, int y) { while (y!=0) { int temp = x%y; x = y; y = temp; } return x; }'}

## 📄 Page 6 - No Heading Found

- {'id': 'p5', 'text': 'Example: Computing GCD(48,120) temp x y After 0 rounds -- 72 120 After 1 round 72 120 72 After 2 rounds 48 72 48 After 3 rounds 24 48 24 After 4 rounds 0 24 0 Output: 24 while (y!=0) { int temp = x%y; x = y; y = temp; }'}

## 📄 Page 7 - No Heading Found

- {'id': 'p6', 'text': '• Theorem: When Euclid’s GCD algorithm terminates, it returns the mathematical GCD of x and y. • Notation: Let g be the GCD of the original values of x and y. • Loop Invariant Lemma: For all k ≥0, The values of x, y after k rounds of the loop satisfy GCD(x,y)=g. • Proof of lemma: ? • Proof of Theorem: The method returns when y=0. By the loop invariant lemma, at this point GCD(x,y)=g. But GCD(x,0)=x for every integer x (since x|0 and x|x). Thus g=x, which is the value returned by the code. • Still Missing: The algorithm always terminates.'}

## 📄 Page 8 - No Heading Found

- {'id': 'p7', 'text': '• Loop Invariant Lemma: For all k ≥0, The values of x, y after k rounds of the loop satisfy GCD(x,y)=g. • Proof: By induction on k. – For k=0, x and y are the original values so clearly GCD(x,y)=g. – Induction step: Let x, y denote that values after k rounds and x’, y’ denote the values after k+1 rounds. We need to show that GCD(x,y)=GCD(x’,y’). According to the code: x’=y and y’=x%y, so the lemma follows from the following mathematical lemma. • Lemma: For all integers x, y: GCD(x, y) = GCD(x%y, y) • Proof: Let x=ay+b, where y>b≥0. I.e. x%y=b. – (1) Since g|y, and g|x, we also have g|(x-ay), I.e. g|b. Thus GCD(b,y) ≥ g = GCD(x,y). – (2) Let g’=GCD(b,y), then g’|(x-ay) and g’|y, so we also have g’|x. Thus GCD(x,y) ≥g’=GCD(b,y).'}

## 📄 Page 9 - No Heading Found

- {'id': 'p8', 'text': '• Why does this algorithm terminate? – After any iteration we have that x > y since the new value of y is the remainder of division by the new value of x. – In further iterations, we replace (x, y) with (y, x%y), and x%y < x, thus the numbers decrease in each iteration. – Formally, the value of xy decreases each iteration (except, maybe, the first one). When it reaches 0, the algorithm must terminate. public static int gcd(int x, int y) { while (y!=0) { int temp = x%y; x = y; y = temp; } return x; }'}

## 📄 Page 10 - No Heading Found

- {'id': 'p9', 'text': '• The problem we want to address is to compute the square root of a real number. • When working with real numbers, we can not have complete precision. – The inputs will be given in finite precision – The outputs should only be computed approximately • The square root problem: – Input: a positive real number x, and a precision requirement ε – Output: a real number r such that |r-√x|≤ε'}

## 📄 Page 11 - No Heading Found

- {'id': 'p10', 'text': 'public static double sqrt(double x, double epsilon){ double low = 0; double high = x>1 ? x : 1; while (high-low > epsilon) { double mid = (high+low)/2; if (mid*mid > x) high = mid; else low = mid; } return low; }'}

## 📄 Page 12 - No Heading Found

- {'id': 'p11', 'text': 'Example: Computing sqrt(2) with precision 0.05: mid mid*mid low high After 0 rounds -- -- 0 2 After 1 round 1 1 1 2 After 2 rounds 1.5 2.25 1 1.5 After 3 rounds 1.25 1.56.. 1.25 1.5 After 4 rounds 1.37.. 1.89.. 1.37.. 1.5 After 5 rounds 1.43.. 2.06.. 1.37.. 1.43.. After 6 rounds 1.40.. 1.97.. 1.40.. 1.43.. Output: 1.40… while (high-low > epsilon) { double mid = (high+low)/2; if (mid*mid > x) high = mid; else low = mid; }'}

## 📄 Page 13 - No Heading Found

- {'id': 'p12', 'text': '• Theorem: When the algorithm terminates it returns a value r that satisfies |r- √x|≤ε. • Loop invariant lemma: For all k ≥0, The values of low, high after k rounds of the loop satisfy: low ≤√x ≤high. • Proof of Lemma: – For k=0, clearly low=0 ≤√x ≤ high=max(x,1). – Induction step: The code only sets low=mid if mid ≤√x, and only sets high=mid if mid>√x. • Proof of Theorem: The algorithm terminates when high-low≤ε, and returns low. At this point, by the lemma: low ≤√x ≤ high ≤ low+ε. Thus |low-√x|≤ε. • Missing Part: Does the algorithm always terminate? How Fast? We will deal with this later.'}

## 📄 Page 14 - No Heading Found

- {'id': 'p13', 'text': '• The running time of your program will depend upon: – The algorithm – The input – Your implementation of the algorithm in a programming language – The compiler you use – The OS on your computer – Your computer hardware – Maybe other things: other programs on your computer; … • Our Motivation: analyze the running time of an algorithm as a function of only simple parameters of the input.'}

## 📄 Page 15 - No Heading Found

- {'id': 'p14', 'text': '• Each algorithm performs a sequence of basic operations: – Arithmetic: (low + high)/2 – Comparison: if ( x > 0 ) … – Assignment: temp = x – Branching: while ( true ) { … } – … • Idea: count the number of basic operations performed on the input. • Difficulties: – Which operations are basic? – Not all operations take the same amount of time. – Operations take different times with different hardware or compilers'}

## 📄 Page 16 - No Heading Found

- {'id': 'p15', 'text': '• Operation counts are only problematic in terms of constant factors. • The general form of the function describing the running time is invariant over hardware, languages or compilers! • Running time is “about” . • We use “Big-O” notation, and say that the running time is O( N2 ) public static int myMethod(int N){ int sq = 0; for(int j=0; j<N ; j++) for(int k=0; k<N ; k++) sq++; return sq; }'}

## 📄 Page 18 - No Heading Found

- {'id': 'p17', 'text': '• Definition: Let f and g be functions from the natural numbers to the natural numbers. We write f=O(g) if there exists a constant c such that for all n: f(n) ≤ cg(n). f=O(g) ⇔ ∃c∀n: f(n) ≤ cg(n) • This is a mathematically formal way of ignoring constant factors, and looking only at the “shape” of the function. • f=O(g) should be considered as saying that “f is at most g, up to constant factors”. • We usually will have f be the running time of an algorithm and g a nicely written function. E.g. The running time of the previous algorithm was O(N^2).'}

## 📄 Page 19 - No Heading Found

- {'id': 'p18', 'text': '• We usually embark on an asymptotic worst case analysis of the running time of the algorithm. • Asymptotic: – Formal, exact, depends only on the algorithm – Ignores constants – Applicable mostly for large input sizes • Worst Case: – Bounds on running time must hold for all inputs. – Thus the analysis considers the worst-case input. – Sometimes the “average” performance can be much better – Real-life inputs are rarely “average” in any formal sense'}

## 📄 Page 20 - No Heading Found

- {'id': 'p19', 'text': '• How fast does Euclid’s algorithm terminate? – After the first iteration we have that x > y. In each iteration, we replace (x, y) with (y, x%y). – In an iteration where x>1.5y then x%y < y < 2x/3. – In an iteration where x ≤1.5y then x%y ≤y/2 < 2x/3. – Thus, the value of xy decreases by a factor of at least 2/3 each iteration (except, maybe, the first one). public static int gcd(int x, int y) { while (y!=0) { int temp = x%y; x = y; y = temp; } return x; }'}

## 📄 Page 21 - No Heading Found

- {'id': 'p20', 'text': '• Theorem: Euclid’s GCD algorithm runs it time O(N), where N is the input length (N=log 2 x + log 2 y). • Proof: – Every iteration of the loop (except maybe the first) the value of xy decreases by a factor of at least 2/3. Thus after k+1 iterations the value of xy is at most the original value. – Thus the algorithm must terminate when k satisfies: – (for the original values of x, y). – Thus the algorithm runs for at most iterations. – Each iteration has only a constant L number of operations, thus the total number of operations is at most – Formally, – Thus the running time is O(N). k'}
- {'id': 'p21', 'text': 'k'}
- {'id': 'p22', 'text': '2 / 3'}
- {'id': 'p23', 'text': '2 / 3'}
- {'id': 'p24', 'text': '2 2 2 / 3'}

## 📄 Page 22 - No Heading Found

- {'id': 'p25', 'text': 'Algorithm: a method or a process followed to solve a problem. – A recipe. A problem is a mapping of input to output. An algorithm takes the input to a problem (function) and transforms it to the output. A problem can have many algorithms.'}

## 📄 Page 23 - No Heading Found

- {'id': 'p26', 'text': 'An algorithm possesses the following properties: – It must be correct. – It must be composed of a series of concrete steps. – There can be no ambiguity as to which step will be performed next. – It must be composed of a finite number of steps. – It must terminate. A computer program is an instance, or concrete representation, for an algorithm in some programming language.'}

## 📄 Page 24 - No Heading Found

- {'id': 'p27', 'text': '• To compare two sorting algorithms, should we talk about how fast the algorithms can sort 10 numbers, 100 numbers or 1000 numbers? • We need a way to talk about how fast the algorithm grows or scales with the input size. – Input size is usually called n – An algorithm can take 100n steps, or 2n2 steps, which one is better?'}

## 📄 Page 25 - No Heading Found

- {'id': 'p28', 'text': '• We want to express the concept of “about”, but in a mathematically rigorous way • Limits are useful in proofs and performance analyses • Θ notation: Θ(n2) = “this function grows similarly to n2”. • Big-O notation: O (n2) = “this function grows at least as slowly as n2”. – Describes an upper bound.'}

## 📄 Page 26 - No Heading Found

- {'id': 'p29', 'text': '• What does it mean? – If f(n) = O(n2), then: • f(n) can be larger than n2 sometimes, but… • I can choose some constant c and some value n 0 such that for every value of n larger than n 0 : f(n) < cn2 • That is, for values larger than n 0 , f(n) is never more than a constant multiplier greater than n2 • Or, in other words, f(n) does not grow more than a constant factor faster than n2.'}
- {'id': 'p30', 'text': '0 0 all for 0 such that and constants positive exist there : n n n cg n f n c n g O n f ≥ ≤ ≤ ='}

## 📄 Page 27 - No Heading Found

- {'id': 'p31', 'text': 'n 0 cg(n) f(n)'}

## 📄 Page 28 - No Heading Found

- {'id': 'p32', 'text': 'Big-O'}
- {'id': 'p33', 'text': '2 1 . 2 2 3 2 2 2 2 2 2 2 2 20 7 5 000 , 150 000 , 000 , 1 2 n O n n O n n O n n n O n n O n ≠ ≠ + = + + = + ='}

## 📄 Page 29 - No Heading Found

- {'id': 'p34', 'text': 'More Big-O • Prove that: • Let c = 21 and n 0 = 4 • 21n2 > 20n2 + 2n + 5 for all n > 4 n2 > 2n + 5 for all n > 4 TRUE'}
- {'id': 'p35', 'text': '2 2 5 2 20 n O n n = + +'}

## 📄 Page 31 - No Heading Found

- {'id': 'p37', 'text': '• Ω() – A lower bound – n2 = Ω(n) – Let c = 1, n 0 = 2 – For all n ≥ 2, n2 > 1 × n ( ) ( ) ( ) ( ) ( ) 0 0 all for 0 such that and constants positive exist there : n n n cg n f n c n g n f ≥ ≥ ≤ Ω ='}

## 📄 Page 32 - No Heading Found

- {'id': 'p38', 'text': 'n 0 cg(n) f(n)'}

## 📄 Page 33 - No Heading Found

- {'id': 'p39', 'text': '• Big-O is not a tight upper bound. In other words n = O(n2) • Θ provides a tight bound • In other words, ( ) ( ) ( ) ( ) ( ) ( ) 0 2 1 0 2 1 all for 0 such that and , , constants positive exist there : n n n g c n f n g c n c c n g n f ≥ ≤ ≤ ≤ Θ = ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) n g n f n g O n f n g n f Ω = = ⇒ Θ = AND'}

## 📄 Page 34 - No Heading Found

- {'id': 'p40', 'text': 'n 0 c 2 g(n) f(n) c 1 g(n)'}

## 📄 Page 36 - No Heading Found

- {'id': 'p42', 'text': '• Little o – A non-tight asymptotic upper bound – n = o(n2), n = O(n2) – 3n2 ≠ o(n2), 3n2 = O(n2) • Ω() – A lower bound – Similar definition to Big-O – n2 = Ω(n) • ω() – A non-tight asymptotic lower bound • f(n) = Θ(n) ⇔ f(n) = O(n) and f(n) = Ω(n)'}

## 📄 Page 37 - No Heading Found

- {'id': 'p43', 'text': 'n 0 O(f(n)) f(n) Ω(f(n)) ω(f(n)) o(f(n)) Θ(f(n))'}

## 📄 Page 39 - No Heading Found

- {'id': 'p45', 'text': '• Prove that: • Let c = 21 and n 0 = 10 • 21n3 > 20n3 + 7n + 1000 for all n > 10 n3 > 7n + 5 for all n > 10 TRUE, but we also need… • Let c = 20 and n 0 = 1 • 20n3 < 20n3 + 7n + 1000 for all n ≥ 1 TRUE'}
- {'id': 'p46', 'text': '3 3'}

## 📄 Page 41 - No Heading Found

- {'id': 'p48', 'text': 'Example 1: a = b; This assignment takes constant time, so it is Θ(1). Example 2: sum = 0; for (i=1; i<=n; i++) sum += n;'}

## 📄 Page 42 - No Heading Found

- {'id': 'p49', 'text': 'Space bounds can also be analyzed with asymptotic complexity analysis. Time: Algorithm Space: Data Structure'}

## 📄 Page 43 - No Heading Found

- {'id': 'p50', 'text': 'One can often reduce time if one is willing to sacrifice space, or vice versa. – Encoding or packing information Boolean flags – Table lookup Factorials Disk-based Space/Time Tradeoff Principle: The smaller you make the disk storage requirements, the faster your program will run.'}