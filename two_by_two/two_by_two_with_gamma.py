{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red140\green211\blue254;\red194\green126\blue101;\red70\green137\blue204;\red89\green138\blue67;\red167\green197\blue152;
\red67\green192\blue160;\red212\green214\blue154;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;\cssrgb\c41569\c60000\c33333;\cssrgb\c70980\c80784\c65882;
\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c66667;}
\margl1440\margr1440\vieww12580\viewh9480\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  dwave.system \cf2 \strokec2 import\cf4 \strokec4  DWaveSampler, EmbeddingComposite\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 sampler_auto = EmbeddingComposite(DWaveSampler(\cf5 \strokec5 solver\cf4 \strokec4 =\{\cf6 \strokec6 'qpu'\cf4 \strokec4 : \cf7 \strokec7 True\cf4 \strokec4 \}))\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf8 \cb3 \strokec8 # Set Q for the problem QUBO\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 # c for coefficient\cf4 \cb1 \strokec4 \
\
\
\
\
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 linear = \{(\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q11'\cf4 \strokec4 ):\cf9 \strokec9 26\cf4 \strokec4 , (\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q12'\cf4 \strokec4 ):\cf9 \strokec9 72\cf4 \strokec4  , (\cf6 \strokec6 'q13'\cf4 \strokec4 ,\cf6 \strokec6 'q13'\cf4 \strokec4 ):-\cf9 \strokec9 6\cf4 \strokec4 , (\cf6 \strokec6 'q14'\cf4 \strokec4 ,\cf6 \strokec6 'q14'\cf4 \strokec4 ):\cf9 \strokec9 8\cf4 \strokec4 , (\cf6 \strokec6 'q21'\cf4 \strokec4 ,\cf6 \strokec6 'q21'\cf4 \strokec4 ):-\cf9 \strokec9 13\cf4 \strokec4 , (\cf6 \strokec6 'q22'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):-\cf9 \strokec9 16\cf4 \strokec4 , (\cf6 \strokec6 'q23'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):\cf9 \strokec9 23\cf4 \strokec4 , (\cf6 \strokec6 'q24'\cf4 \strokec4 ,\cf6 \strokec6 'q24'\cf4 \strokec4 ):\cf9 \strokec9 56\cf4 \strokec4 \}\cb1 \
\
\
\cb3 quadratic = \{(\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q12'\cf4 \strokec4 ):\cf9 \strokec9 40\cf4 \strokec4 , (\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q13'\cf4 \strokec4 ):-\cf9 \strokec9 20+1000\cf4 \strokec4 , (\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q13'\cf4 \strokec4 ):-\cf9 \strokec9 40\cf4 \strokec4 , (\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q14'\cf4 \strokec4 ):-\cf9 \strokec9 40\cf4 \strokec4 , (\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q14'\cf4 \strokec4 ):-\cf9 \strokec9 80+1000\cf4 \strokec4 , (\cf6 \strokec6 'q13'\cf4 \strokec4 ,\cf6 \strokec6 'q14'\cf4 \strokec4 ):\cf9 \strokec9 40\cf4 \strokec4 , (\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q21'\cf4 \strokec4 ):\cf9 \strokec9 2\cf4 \strokec4 , (\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q21'\cf4 \strokec4 ):\cf9 \strokec9 4\cf4 \strokec4 , (\cf6 \strokec6 'q13'\cf4 \strokec4 ,\cf6 \strokec6 'q21'\cf4 \strokec4 ):-\cf9 \strokec9 2\cf4 \strokec4 ,(\cf6 \strokec6 'q14'\cf4 \strokec4 ,\cf6 \strokec6 'q21'\cf4 \strokec4 ):-\cf9 \strokec9 4\cf4 \strokec4 , (\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):\cf9 \strokec9 4\cf4 \strokec4 ,(\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):\cf9 \strokec9 8\cf4 \strokec4 , (\cf6 \strokec6 'q13'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):-\cf9 \strokec9 4\cf4 \strokec4 ,(\cf6 \strokec6 'q14'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):-\cf9 \strokec9 8\cf4 \strokec4 , (\cf6 \strokec6 'q21'\cf4 \strokec4 ,\cf6 \strokec6 'q22'\cf4 \strokec4 ):\cf9 \strokec9 20\cf4 \strokec4 ,(\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):-\cf9 \strokec9 2\cf4 \strokec4 , (\cf6 \strokec6 'q12'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):-\cf9 \strokec9 4\cf4 \strokec4 ,(\cf6 \strokec6 'q13'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):\cf9 \strokec9 2\cf4 \strokec4 , (\cf6 \strokec6 'q14'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):\cf9 \strokec9 4\cf4 \strokec4 ,(\cf6 \strokec6 'q21'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):-\cf9 \strokec9 10+1000\cf4 \strokec4 , (\cf6 \strokec6 'q22'\cf4 \strokec4 ,\cf6 \strokec6 'q23'\cf4 \strokec4 ):-\cf9 \strokec9 20\cf4 \strokec4 ,(\cf6 \strokec6 'q11'\cf4 \strokec4 ,\cf6 \strokec6 'q24'\cf4 \strokec4 ):-\cf9 \strokec9 4, ('q12','q24'):-8,('q13','q24'):4, ('q14','q24'):8,('q21','q24'):-20, ('q22','q24'):-40+1000,(\'91q23','q24'):20\}\cf4 \cb1 \strokec4 \
\
\cb3 Q = \cf10 \strokec10 dict\cf4 \strokec4 (linear)\cb1 \
\cb3 Q.update(quadratic)\cb1 \
\
\
\
\pard\pardeftab720\sl360\partightenfactor0
\cf8 \cb3 \strokec8 # Minor Embed and sample 1000 times on a default D-Wave sytem\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 sampleset = sampler_auto.sample_qubo(Q, \cf5 \strokec5 num_reads\cf4 \strokec4 =\cf9 \strokec9 10000\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf11 \cb3 \strokec11 print\cf4 \strokec4 (sampleset)\cb1 \
}