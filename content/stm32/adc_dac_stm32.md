Title: STM32 Based ADC Board for Electric Guitars (Part I)
Date: 2025-10-26 10:20
Modified: 2025-10-26 10:20
Category: Electronics, STM32
Tags: Electronics, Guitar, Kicad
Slug: adc_dac_stm32
Authors: Cagil Gumus
Summary: Designing an STM32 Based ADC board on KiCAD for electric guitars.
<!-- Status: draft -->

## Why? 

It's the end of 2025 and we still can't connect our guitars to our PCs/Laptops via USB cable..

<!-- Insert pic of a horribly edited guitar with USB port sticking out-->

Looking at the market, we can see that there are not much products like this

<!-- Insert investigation here -->

I'm going to (at least) attempt at doing this myself. Can't be that hard right? 

## How? 

Idea is simple: 

* Take the guitar signal from the pickup. 
* Do some analog electronics stuff to it 
* Digitize it with an ADC 
* Process it with STM32 which streams the Digitized (and maybe even processed) signal towards any OS.
* ????
* Profit

### Overview

<!-- Insert general idea picture-->

Electric guitars give high impedance output which means we can't just connect 
the output of the pickups to the ADC. That would be bad. 

What we need is to 'buffer' it, scale it (gain) and then filter it to get rid of high frequency noise. 

