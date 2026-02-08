<script lang="ts">
  // 1. Import the global CSS (Make sure app.css exists in src/)
  import './layout.css';

  // 2. Capture the page content passed to this layout
  let { children } = $props();
</script>

{@render children()}