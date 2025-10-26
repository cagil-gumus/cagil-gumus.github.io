Title: FWK - Open Source FPGA Framework
Date: 2025-05-25
Category: FPGA
Tags: FPGA
Slug: fwk
Authors: Cagil Gumus
Summary: FWK is an open-source FPGA development framework that I've worked on. But why?

## Ambitions

<iframe width="560" height="315" src="https://www.youtube.com/embed/iDwlSPno13k?si=ib2jf_GGN-mdkc20" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I gave a talk at the [13<sup>th</sup> MicroTCA Workshop](https://mtcaws.desy.de/) at Hamburg/Germany about [FWK](https://gitlab.desy.de/fpgafw/fwk).

In that talk, I went into considerable detail about why and how we developed this EDA abstraction tool.

Due to time limitations, I couldn't dedicate much attention to the 'Why' behind creating such a tool. So now, with my own (useless) blog, I can explain further:

FWK is born due to:

* FPGA development is hard. 
* Scientific research is harder. 
* FPGA development in scientific research could be a nightmare. 

DESY had accumulated nearly a million lines of VHDL code, along with approximately 30,000 lines of Tcl (I sincerely dislike Tcl, and I'm prepared to debate it). This code, developed in-house over time, addressed a multitude of problems. It resided in a single SVN repository with thousands of commits and, predictably, lacked proper documentation and suffered from a rigid structure.

However, in 2020, the team I was part of decided to take this existing framework, rewrite it entirely from scratch, and release it publicly under an open-source license.

It was a bold move.

## Yet another tool

There's one statement I made during the talk that might seem hypocritical:

> ... to avoid reinventing the wheel ...

This is rather funny because FWK is indeed re-inventing a tool. EDA Abstraction tool to be precise.  
There are already other projects:

* [FuseSoC](https://github.com/olofk/fusesoc) + [edalize](https://github.com/olofk/edalize)
* [pyfpga](https://github.com/PyFPGA/pyfpga)
* [hdlmake](https://ohwr.org/projects/hdl-make/)

Is FWK actually better than those tools? I don't think so. However, what our community (Experimental-Physics) often needs is not the *perfect* solution, but a solution that is available and useable. 

FWK is indeed useful. We have seen its adoption at several European facilities, such as HZDR (Dresden, Germany), HZB (Berlin, Germany), and CERN (Geneva, Switzerland). If you are working with MicroTCA hardware, we offer the **only** open-source solution currently available.
There are now over 10 active contributors to this repository and it is growing.


## The future

FWK will change. Most probably drop it's tcl backend and replace it with Python. It also lack package manager capabilities. 
Maybe it will **fuse** with FuseSoc? Who knows?

You can now ask latest AI-overlord models about our tools like FWK and get decent answers on what exactly is FWK.

Making our tools open-source has enabled this. Our name is on the map. 

FWK is enabling science and that's what matters at the end.

<img src="{static}/FPGA/images/fwk_logo_org.svg" width="350">
