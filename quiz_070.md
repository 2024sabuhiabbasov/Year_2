# Quiz 070

<img width="max" alt="Screenshot 2023-09-03 at 16 31 02" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/1a0d4121-8110-4f64-a93e-1efee6d0625c">

## Solution
<img width="max" alt="Screenshot 2023-09-03 at 16 31 42" src="https://github.com/2024sabuhiabbasov/Year_2/assets/111758436/d1835c80-6e8a-4409-8c27-af067dfaaf33">

```.py
class ipv4machine:

    @property
    def generator(self):
        return [f"{i}.{j}.{k}.{l}" for i in range(256) for j in range(256) for k in range(256) for l in range(256)]


ipv4 = ipv4machine()
output = ipv4.generator
print(output)
```
