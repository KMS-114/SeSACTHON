<script>
  import { onMount } from 'svelte';
  import { wrap } from 'svelte-spa-router/wrap';

  export let params; // svelte-spa-router에서 제공하는 동적 파라미터

  let jobId = params.id;
  let jobDetail = null;
  let error = null;

  async function fetchJobDetail() {
    try {
      const response = await fetch(`http://localhost:8000/job-listings/${jobId}`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      jobDetail = await response.json();
    } catch (err) {
      error = err.message;
    }
  }

  onMount(fetchJobDetail);
</script>

<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else if !jobDetail}
    <p>Loading...</p>
  {:else}
    <div class="job-detail">
      <h1>{jobDetail.title}</h1>
      <p><strong>회사:</strong> {jobDetail.company}</p>
      <p><strong>설명:</strong> {jobDetail.description}</p>
    </div>
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
</style>
