    

# Dugeon Crawler

This rogue like game is designed to be be controlled either through the keyboard 
or by using a 'bot' created with JavaScript

## requirements

* python 3
* pipenv

## Install dependencies

```
pipenv install

```

## Start Game

```
pipenv run python src/main.py
```

## Controls

| Key | Descriptions |
| --- | --- |
| Up Arrow | Move up |
| Down Arrow | Move Down |
| Left Arrow | Move Left |
| Right Arrow | Move Right |

## Notes

```
Actor
- controller component
- AI (finite state machine)
-- User controller

Actor -> Hero
Actor -> Enemy

```

```
Game Play

- Actions
-- Use/Item
-- Attack
-- Walk
-- LOS
-- Toss /Throw

```

```
Item System

- Items
-- consumable
-- durable/multi-use
- Weapons
-- short range
-- long range (use toss action)
-- magic??
- Armor
--

```

```
game loops

-- animation
-- movement
-- player controls
-- attacks
-- physics
-- rendering

```


