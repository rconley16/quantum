from dwave.system import DWaveSampler, EmbeddingComposite
import time

sampler_auto = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

# Set Q for the problem QUBO
# c for coefficient




linear = {('q11','q11'):26, ('q12','q12'):72 , ('q13','q13'):-6, ('q14','q14'):8, ('q21','q21'):-13, ('q22','q22'):-16, ('q23','q23'):23, ('q24','q24'):56}


quadratic = {('q11','q12'):40, ('q11','q13'):980, ('q12','q13'):960, ('q11','q14'):960, ('q12','q14'):920, ('q13','q14'):40, ('q11','q21'):2, ('q12','q21'):4, ('q13','q21'):-2,('q14','q21'):-4, ('q11','q22'):4,('q12','q22'):8, ('q13','q22'):-4,('q14','q22'):-8, ('q21','q22'):20,('q11','q23'):-2, ('q12','q23'):-4,('q13','q23'):2, ('q14','q23'):4,('q21','q23'):990, ('q22','q23'):980,('q11','q24'):-4, ('q12','q24'):-8, ('q13','q24'):4, ('q14','q24'):8,('q21','q24'):980, ('q22','q24'):960,('q23','q24'):20}

Q = dict(linear)
Q.update(quadratic)



# Minor Embed and sample 10 times on a default D-Wave sytem, repeat up to 100 times
#   or until the lowest energy is found
tic = time.perf_counter()
for i in range(1,100):
    sampleset = sampler_auto.sample_qubo(Q, num_reads=10)
    print(sampleset)
    print(sampleset.first[1])
    if sampleset.first[1] == -26:
        print("Lowest energy was reached. \n")
        print("This took {0} samples of 10".format(i))
        break
toc = time.perf_counter()
print(f"Found the lowest energy in {toc - tic:0.10f} seconds")
print(sampleset.first)