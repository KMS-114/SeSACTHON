<!-- <script>
  import { onMount } from 'svelte';
  import { location } from 'svelte-routing';

  export let id;
  export let job = null;
  let error = null;

  // This part is used when job is not provided as a prop
  async function fetchJobDetail(id) {
    try {
      const response = await fetch(`http://localhost:8000/job-listings/${id}`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      job = await response.json();
    } catch (err) {
      error = err.message;
    }
  }

  // Fetch job detail if job is not passed as a prop
  onMount(() => {
    if (!job) {
      fetchJobDetail(id);
    }
  });
</script>

<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else if job}
    <h1>{job.title}</h1>
    <p><strong>회사:</strong> {job.company}</p>
    <p><strong>설명:</strong> {job.description}</p>
  {/if}
</main>


<style>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'LotteMartDream', sans-serif;
  }

  .error {
    color: red;
    text-align: center;
  }

  .job-detail {
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-top: 20px;
  }

  h1 {
    margin-top: 0;
    color: #007BFF;
  }

  p {
    margin: 10px 0;
    color: #555;
  }

  p strong {
    color: #333;
  }
</style> -->
