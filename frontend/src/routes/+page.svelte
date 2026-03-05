<script>
  import { onMount, onDestroy } from 'svelte';

  let showCVModal = false;

  function randHex() {
    return '0x' + Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
  }
  function randRow() {
    return Array.from({ length: 8 }, randHex).join(' ');
  }

  let hexRows = [
    '0x45 0x00 0x00 0x3c 0x1c 0x46 0x40 0x00',
    '0x40 0x06 0xb1 0xe6 0xc0 0xa8 0x00 0x68',
    '0xc0 0xa8 0x00 0x01 0x00 0x00 0x00 0x00',
  ];
  let latency = '0.4';

  // Fade visibility for each line: [panic, optimal, latency, connection]
  let vis = [true, true, true, true];

  const intervals = [];

  onMount(() => {
    // Fast hex cycling
    intervals.push(setInterval(() => {
      hexRows = hexRows.map(() => Math.random() > 0.4 ? randRow() : randRow());
      latency = (Math.random() * 0.9 + 0.1).toFixed(2);
    }, 120));

    // Each status line fades independently on random timers
    [0, 1, 2, 3].forEach((i) => {
      const cycle = () => {
        vis[i] = false;
        vis = [...vis];
        const holdOff = 400 + Math.random() * 800;
        setTimeout(() => {
          vis[i] = true;
          vis = [...vis];
          setTimeout(cycle, 1500 + Math.random() * 3000);
        }, holdOff);
      };
      setTimeout(cycle, 1000 + Math.random() * 3000);
    });
  });

  onDestroy(() => intervals.forEach(clearInterval));

  function handleCVClick(e) {
    e.preventDefault();
    showCVModal = true;
  }

  function closeCVModal() {
    showCVModal = false;
    document.getElementById('experience').scrollIntoView({ behavior: 'smooth' });
  }
</script>

<svelte:head>
  <title>Mariesha Zara Murphy | Quant Platform Engineer</title>
</svelte:head>

{#if showCVModal}
  <div class="fixed inset-0 z-[100] flex items-center justify-center bg-black/70 backdrop-blur-sm" role="dialog" aria-modal="true">
    <div class="bg-[#0f172a] border border-white/10 p-8 max-w-md w-full mx-4 font-mono">
      <p class="text-[10px] text-purple-400 uppercase tracking-widest mb-4">// ACCESS_LOGS</p>
      <p class="text-white font-bold mb-2">CV not publicly hosted.</p>
      <p class="text-slate-400 text-sm mb-6 leading-relaxed">
        To protect against automated scraping, my CV is available on direct request only.<br><br>
        Contact: <a href="mailto:mzaramurphy@gmail.com" class="text-blue-400 hover:text-white transition">mzaramurphy@gmail.com</a>
      </p>
      <button onclick={closeCVModal} class="font-mono text-xs font-bold py-2 px-5 border border-white/20 text-white hover:bg-white/5 transition">
        VIEW_EXPERIENCE →
      </button>
    </div>
  </div>
{/if}

<div class="min-h-screen font-sans selection:bg-purple-500 selection:text-white bg-[#020617]">

  <nav class="sticky top-0 z-50 border-b border-white/5 bg-[#020617]/90 backdrop-blur-md px-4 sm:px-6 py-3 sm:py-4">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
        <div class="flex items-center gap-3">
            <div class="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
            <span class="font-mono text-white font-bold tracking-tight text-sm">MZM_PORTFOLIO</span>
        </div>
        
        <div class="flex gap-3 sm:gap-6 text-[9px] sm:text-[10px] font-mono font-bold tracking-tight sm:tracking-widest">
            <a href="#projects" class="text-white hover:text-blue-400 transition">./PROJECTS</a>
            <a href="#experience" class="text-slate-500 hover:text-purple-400 transition">./EXPERIENCE</a>
            <a href="mailto:mzaramurphy@gmail.com" class="text-slate-500 hover:text-green-400 transition">./CONTACT</a>
        </div>
    </div>
  </nav>

  <header class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
    <div>
      <h1 class="text-5xl md:text-6xl font-bold text-white mb-4 tracking-tight leading-tight">
        Mariesha Zara Murphy
      </h1>
      
      <p class="font-mono text-purple-400 text-lg mb-6">
        Quant Platform Engineer // Systems & Networks
      </p>
      
      <p class="text-xl text-slate-400 mb-8 max-w-lg leading-relaxed">
        Incoming <span class="text-blue-400 font-medium">Quant Platform Engineer</span> bridging the gap between hardware/kernel operations and hyperscale cloud architectures.
      </p>
      
      <div class="flex flex-wrap gap-4">
        <a href="#projects" class="font-mono text-xs font-bold py-3 px-6 bg-white text-black hover:bg-blue-400 hover:text-white transition duration-200">
            VIEW_SYSTEMS
        </a>
        <button onclick={handleCVClick} class="font-mono text-xs font-bold py-3 px-6 border border-white/20 text-white hover:bg-white/5 transition duration-200">
            ACCESS_LOGS (CV)
        </button>
      </div>
      
      <div class="mt-8 flex gap-4 font-mono text-xs uppercase tracking-widest">
        <a href="https://github.com/MZMurphy" class="text-blue-400 hover:text-white transition">GitHub: @MZMurphy</a>
        <span class="text-slate-700">|</span>
        <a href="https://linkedin.com/in/mariesha-zara-murphy" class="text-blue-400 hover:text-white transition">LinkedIn: /in/mariesha-zara-murphy</a>
      </div>
    </div>
    
    <div class="hidden md:block font-mono text-[13px] text-right text-slate-600 select-none leading-relaxed self-center mt-16">
      <span class="block transition-opacity duration-300" style="opacity: 0.6">{hexRows[0]}</span>
      <span class="block transition-opacity duration-300" style="opacity: 0.6">{hexRows[1]}</span>
      <span class="block transition-opacity duration-300" style="opacity: 0.6">{hexRows[2]}</span>
      <span class="block transition-opacity duration-500 mt-1" style="opacity: {vis[0] ? 0.5 : 0}">// KERNEL_PANIC_PREVENTED</span>
      <span class="block transition-opacity duration-500" style="opacity: {vis[1] ? 0.5 : 0}">// SYSTEM_OPTIMAL</span>
      <span class="block transition-opacity duration-500" style="opacity: {vis[2] ? 0.5 : 0}">// LATENCY: {latency}ms</span>
      <span class="block transition-opacity duration-700 mt-1 text-blue-500" style="opacity: {vis[3] ? 0.9 : 0}">Connection established: Handshake complete.</span>
    </div>
  </header>

  <main id="projects" class="max-w-7xl mx-auto px-6 mb-24">
    <div class="flex items-center gap-4 mb-12">
      <h2 class="font-mono text-xs font-bold text-slate-500 uppercase tracking-widest">Active_Deployments</h2>
      <div class="h-px bg-slate-800 flex-grow"></div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

      <!-- 1. DeepDig -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./bin/debug</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-purple">active</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
          <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ VIDEO: DEEPDIG_DEMO.WEBM ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">DeepDig Debugger</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Low-level Linux binary debugger. Pure C core for kernel interfacing via ptrace API with DWARF symbol parsing.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
            <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-cpp">C++20</span>
            <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-c">C</span>
            <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ptrace">PTRACE</span>
            <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ptrace">Linux</span>
          </div>
        </div>
      </article>

      <!-- 2. Cloud-Comfort -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./cloud/infra</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-blue">active</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ VIDEO: CLOUD_COMFORT_DEMO.WEBM ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">Cloud-Comfort</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Agentic AI environment for cloud infrastructure. Parses Terraform into animated React Flow diagrams. Built on AWS internship knowledge to keep diagrams intuitive and production-accurate. Overhauled frontend with file sidebar, resource count bar, and minimap for large topologies.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-go">Go</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ts">TypeScript</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-terraform">Terraform</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-react">React Flow</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-aws">AWS</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-gcp">GCP</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-azure">Azure</span>
          </div>
        </div>
      </article>

      <!-- 3. Portfolio Website -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./web/deploy</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-blue">production</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ VIDEO: PORTFOLIO_DEMO.WEBM ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">Portfolio Website</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            This site. SvelteKit frontend deployed to AWS via a Python CDK stack — S3 origin behind a CloudFront distribution with HTTPS enforced and cache invalidation on deploy. Full infrastructure-as-code from scratch.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-svelte">SvelteKit</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-python">Python CDK</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-aws">AWS</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ts">TypeScript</span>
          </div>
        </div>
      </article>

      <!-- 4. AWS Edge Automation -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./aws/infra</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-blue">production</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ VIDEO: CLOUD_TOPOLOGY.WEBM ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">AWS Edge Automation</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Security-as-Code stack for global SD-WAN. Automated production infrastructure using TypeScript constructs.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-python">Python</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ts">TypeScript</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-aws">CDK</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-aws">AWS</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-aws">Lambda</span>
          </div>
        </div>
      </article>

      <!-- 5. HeapHeaver -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./mem/check</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-purple">opensource</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ VIDEO: MEMORY_LEAK.WEBM ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">HeapHeaver</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
             Valgrind-inspired memory leak detection engine. Supports flow control and verbose debugging for C binaries.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-rust">RUST</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-c">C</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ptrace">Linux</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ptrace">LD_PRELOAD</span>
             <span class="font-mono text-[10px] bg-slate-900 border px-2 py-1 tag-ptrace">dlsym</span>
          </div>
        </div>
      </article>

      <!-- 6. Placeholder -->
      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./???/pending</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-purple">incoming</span>
        </div>
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">[ CLASSIFIED ]</span>
        </div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">???</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Project details redacted. Deployment imminent.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">REDACTED</span>
          </div>
        </div>
      </article>

    </div>
  </main>

  <div class="max-w-7xl mx-auto px-6 mt-32 grid grid-cols-1 md:grid-cols-2 gap-16">

    <section id="experience">
      <h2 class="font-mono text-xs font-bold text-slate-500 mb-12 uppercase tracking-[0.3em]">Experience Audit</h2>
      <div class="border-l border-white/10 ml-2">
          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-purple-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">Incoming Quant Platform Engineer</h4>
              <p class="font-mono text-[10px] text-purple-400 uppercase">Confidential Firm // 2026</p>
          </div>

          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-blue-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">Network Development Engineer Intern</h4>
              <p class="font-mono text-[10px] text-blue-400 uppercase">Amazon Web Services (AWS) // 2025</p>
              <p class="text-slate-500 text-sm mt-2 leading-relaxed">
                  Automated production network provisioning and management via IaC. Edge Network Cloud team focus.
              </p>
          </div>

          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-slate-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">Secure Software Developer Intern</h4>
              <p class="font-mono text-[10px] text-slate-400 uppercase">HMG Civil Service // 2024 - 2025</p>
              <p class="text-slate-500 text-sm mt-2 leading-relaxed">
                  Developed POSIX-compliant C/C++ developer utilities for Linux and Unix based Hypervisor systems
              </p>
          </div>
      </div>
    </section>

    <section>
      <h2 class="font-mono text-xs font-bold text-slate-500 mb-12 uppercase tracking-[0.3em]">Attended_Events</h2>
      <div class="border-l border-white/10 ml-2">
          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-purple-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">AWS // SRE Events</h4>
              <p class="font-mono text-[10px] text-purple-400 uppercase">Incoming // 2026</p>
          </div>

          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-blue-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">HackEurope Stockholm</h4>
              <p class="font-mono text-[10px] text-blue-400 uppercase">Hackathon // 2026</p>
              <p class="text-slate-500 text-sm mt-2 leading-relaxed">Built Cloud-Comfort.</p>
          </div>

          <div class="mb-10 pl-8 relative">
              <div class="absolute w-2 h-2 bg-slate-500 -left-[5px] top-1"></div>
              <h4 class="text-white font-bold">HackTheBox Events</h4>
              <p class="font-mono text-[10px] text-slate-400 uppercase">CTF // Ongoing</p>
          </div>
      </div>
    </section>

  </div>

  <footer class="max-w-7xl mx-auto mt-40 pb-20 border-t border-white/5 pt-10 flex justify-between items-center text-[10px] font-mono text-slate-600 px-6">
    <div>MARIESHA ZARA MURPHY // GRAD_2026</div>
    <div>SYSTEM_READY</div>
  </footer>

</div>