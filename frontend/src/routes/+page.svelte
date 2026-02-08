<svelte:head>
  <title>Mariesha Zara Murphy | Quant Platform Engineer</title>
</svelte:head>

<div class="min-h-screen font-sans selection:bg-purple-500 selection:text-white bg-[#020617]">

  <nav class="sticky top-0 z-50 border-b border-white/5 bg-[#020617]/90 backdrop-blur-md px-6 py-4">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
        <div class="flex items-center gap-3">
            <div class="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
            <span class="font-mono text-white font-bold tracking-tight text-sm">MZM_PORTFOLIO</span>
        </div>
        
        <div class="flex gap-6 text-[10px] font-mono font-bold tracking-widest">
            <a href="#projects" class="text-white hover:text-blue-400 transition">./PROJECTS</a>
            <a href="#experience" class="text-slate-500 hover:text-purple-400 transition">./EXPERIENCE</a>
            <a href="mailto:hello@example.com" class="text-slate-500 hover:text-green-400 transition">./CONTACT</a>
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
        <a href="#experience" class="font-mono text-xs font-bold py-3 px-6 border border-white/20 text-white hover:bg-white/5 transition duration-200">
            ACCESS_LOGS (CV)
        </a>
      </div>
      
      <div class="mt-8 flex gap-4 font-mono text-xs uppercase tracking-widest">
        <a href="https://github.com/mariesha" class="text-blue-400 hover:text-white transition">GitHub: @mariesha</a>
        <span class="text-slate-700">|</span>
        <a href="https://linkedin.com/in/mariesha-zara-murphy" class="text-blue-400 hover:text-white transition">LinkedIn: /in/mariesha-zara-murphy</a>
      </div>
    </div>
    
    <div class="hidden md:block font-mono text-[10px] text-right text-slate-600 select-none opacity-50 leading-tight">
      0x45 0x00 0x00 0x3c 0x1c 0x46 0x40 0x00 <br>
      0x40 0x06 0xb1 0xe6 0xc0 0xa8 0x00 0x68 <br>
      0xc0 0xa8 0x00 0x01 0x00 0x00 0x00 0x00 <br>
      // KERNEL_PANIC_PREVENTED <br>
      // SYSTEM_OPTIMAL <br>
      // LATENCY: 0.4ms <br>
      <span class="text-blue-500">Connection established: Handshake complete.</span>
    </div>
  </header>

  <main id="projects" class="max-w-7xl mx-auto px-6 mb-24">
    <div class="flex items-center gap-4 mb-12">
      <h2 class="font-mono text-xs font-bold text-slate-500 uppercase tracking-widest">Active_Deployments</h2>
      <div class="h-px bg-slate-800 flex-grow"></div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./bin/debug</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-purple">active</span>
        </div>
        
        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
          <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">
            [ VIDEO: DEEPDIG_DEMO.WEBM ]
          </span>
        </div>
        
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">DeepDig Debugger</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Low-level Linux binary debugger. Pure C core for kernel interfacing via ptrace API with DWARF symbol parsing.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
            <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">C++20</span>
            <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">PTRACE</span>
          </div>
        </div>
      </article>

      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./aws/infra</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-blue">production</span>
        </div>

        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">
             [ VIDEO: CLOUD_TOPOLOGY.WEBM ]
           </span>
        </div>
        
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">AWS Edge Automation</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
            Security-as-Code stack for global SD-WAN. Automated production infrastructure using TypeScript constructs.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">CDK</span>
             <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">TS</span>
          </div>
        </div>
      </article>

      <article class="project-card rounded overflow-hidden flex flex-col h-full">
        <div class="termbar px-4 py-2 flex justify-between items-center">
            <span class="font-mono text-[10px] text-slate-400">./mem/check</span>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded badge-purple">opensource</span>
        </div>

        <div class="h-48 bg-black border-b border-white/5 flex items-center justify-center overflow-hidden relative">
           <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10 pointer-events-none"></div>
           <span class="font-mono text-slate-700 text-[10px] text-center px-4 relative z-0">
             [ VIDEO: MEMORY_LEAK.WEBM ]
           </span>
        </div>
        
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-lg font-bold text-white mb-2">HeapHeaver</h3>
          <p class="text-sm text-slate-400 mb-6 leading-relaxed flex-grow">
             Valgrind-inspired memory leak detection engine. Supports flow control and verbose debugging for C binaries.
          </p>
          <div class="flex flex-wrap gap-2 mt-auto">
             <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">RUST</span>
             <span class="font-mono text-[10px] bg-slate-900 border border-white/5 px-2 py-1 text-slate-300">C</span>
          </div>
        </div>
      </article>

    </div>
  </main>

  <section id="experience" class="max-w-4xl mx-auto px-6 mt-32">
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
                Automated production network management via IaC. Edge Network Cloud team focus.
            </p>
        </div>

        <div class="mb-10 pl-8 relative">
            <div class="absolute w-2 h-2 bg-slate-500 -left-[5px] top-1"></div>
            <h4 class="text-white font-bold">Secure Software Developer Intern</h4>
            <p class="font-mono text-[10px] text-slate-400 uppercase">HMG Civil Service // 2024 - 2025</p>
            <p class="text-slate-500 text-sm mt-2 leading-relaxed">
                POSIX-compliant C/C++ utilities. High-security virtualized environments.
            </p>
        </div>
    </div>
  </section>

  <footer class="max-w-7xl mx-auto mt-40 pb-20 border-t border-white/5 pt-10 flex justify-between items-center text-[10px] font-mono text-slate-600 px-6">
    <div>MARIESHA ZARA MURPHY // GRAD_2026</div>
    <div>SYSTEM_READY</div>
  </footer>

</div>