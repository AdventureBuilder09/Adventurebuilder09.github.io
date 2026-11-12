---
---
<div id="build-status">Checking commit status...</div>

<script>
fetch('https://api.github.com/repos/Adventurebuilder09/adventurebuilder09.github.io/commits/main')

    .then(response => response.json())

    .then(data => {

      const latestCommitDate = new Date(data.commit.committer.date);

      document.getElementById('build-status').innerText =

        `Last commit time: ${latestCommitDate.toLocaleString()}`;

    })

    .catch(error => {

      document.getElementById('build-status').innerText = 'Could not get last commit date.';

    });
</script>

<p>Last site build time: {{ site.time | date: "%m/%d/%Y, %H:%M:%S" }}</p>
A place for me to put stuff on the internet
- [Magic: the Gathering custom format: Points based Kernel (KP)](Kernel/Kernel%20Points) - [Web Link](https://adventurebuilder09.github.io/Kernel/Kernel%20Points.html)
	- [Kernel Deck Checker (Functional)](Kernel/Parse/Kernel-Validity-Checker.html)
	- [A list of KP decks](Kernel/A%20List%20Of%20KP%20Decks)
- [Mage Duels - WIP TCG](Mage%20Duels/Overview)
- [Desmos Archive](Desmos Archive)
- [Fosthoumb - Audio synthesis class final project](https://soundcloud.com/william-green-189440192/fosthoumb) 
	- [Anonymous Upload](https://soundcloud.com/anon-320118416/fosthoumb)