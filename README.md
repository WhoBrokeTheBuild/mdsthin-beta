
# mdsthin - Python MDSplus Thin Client Implementation

## Installation

```sh
git clone https://github.com/WhoBrokeTheBuild/mdsthin-beta.git
python3 -m pip install -e mdsthin-beta
```

## Tests

```sh
python3 -m mdsthin.test [-v] [--server SERVER] [--cmod]
```

## Usage

**Connection**

```py
import mdsthin
c = mdsthin.Connection('server')


print(c.get('whoami()').data())
# username

print(c.tcl('show current test'))
# 123

print(c.get('4 + 5').data())
# 9


c.openTree('test', 123)


y = c.get('SIGNAL_NODE').data()
x = c.get('dim_of(SIGNAL_NODE)').data()


gm = c.getMany()
gm.append('y', 'SIGNAL_NODE')
gm.append('x', 'dim_of(SIGNAL_NODE)')
gm.execute()

y = gm.get('y')
x = gm.get('x')


print(c.getObject('ACTION_NODE').data())
# Action(...)

```

**mdstcl**

```
python3 -m mdsthin.mdstcl SERVER
Connectiong to: SERVER
TCL> show current test
123
TCL> exit
```

```py
import mdsthin
c = mdsthin.Connection('server')

c.mdstcl()
TCL> show current test
123
TCL> exit
```

**tdic**

```
python3 -m mdsthin.tdic SERVER
Connectiong to: SERVER
TDI> 4 + 5
9
TDI> exit
```

```py
import mdsthin
c = mdsthin.Connection('server')

c.tdic()
Connectiong to: SERVER
TDI> 4 + 5
9
TDI> exit
```
