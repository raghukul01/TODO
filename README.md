# TODO
Command line tool to manage you TODOs.

This readme provide insights on installation, usage etc for __Ubuntu__, for other OS process is similar.

## Installing

### Prerequisites
- [Git](https://git-scm.com)
- python

For __Ubuntu__ you can install by:

    $: git clone https://github.com/raghukul01/TODO.git
    $: chmod +x install.sh
    $: source install.sh
    
## Uninstalling

    $: chmod +x uninstall.sh
    $: source uninstall.sh
    
## Usage

Typing todo on prompt simply prints all the task in TODO list.

    $: todo
    ===      :TODOS:      ===
    No TODOs now, enjoy!!
    =========================

Also you can use following commands to modify your TODO list.

 - ### add
   This command adds a new (or a list of) task (tasks) into your __TODO__ list.
   
       $: todo add "Complete Documentation" 
       =====      :TODOS:      =====
       1: Complete Documentation
       =============================
   
       $: todo add "push code to github" "get feedback from community" "repeat"  
       ========      :TODOS:      ========
       1: Complete Documentation
       2: push code to github
       3: get feedback from community
       4: repeat
       ===================================
       
 - ### del
   Deletes an item from TODO list. Input can either be task, or task index.
   
       $: todo del "repeat"
       ========      :TODOS:      ========
       1: Complete Documentation
       2: push code to github
       3: get feedback from community
       ===================================
       
       $: todo del 2
       ========      :TODOS:      ========
       1: Complete Documentation
       2: get feedback from community
       ===================================
 - ### clear
   Removes all task from TODO list.
   
       $: todo add "random entry" "random entry 2, which illustrates banner resize"
       ==================      :TODOS:      ==================
       1: Complete Documentation
       2: get feedback from community
       3: random entry
       4: random entry 2, which illustrates banner resize
       =======================================================
       
       $: todo clear
       ===      :TODOS:      ===
       No TODOS now, enjoy!!
       =========================
