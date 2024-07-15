<script>
    import { onMount } from 'svelte';
    import Navbar from '../../components/Navbar.svelte';

    let jobListings = [];
    let filteredJobListings = [];
    let error = null;
    let searchQuery = '';
    let filterCompany = '';
  
    async function fetchJobListings() {
      try {
        const response = await fetch('http://localhost:8000/job-listings');
        if (!response.ok) {
          throw new Error('네트워크 응답이 실패했습니다');
        }
        jobListings = await response.json();
        filteredJobListings = jobListings;
      } catch (err) {
        error = err.message;
      }
    }
  
    function filterJobs() {
      const query = searchQuery.toLowerCase();
      const company = filterCompany.toLowerCase();
  
      filteredJobListings = jobListings.filter(job => {
        const matchesQuery = job.title.toLowerCase().includes(query) || job.description.toLowerCase().includes(query);
        const matchesCompany = company ? job.company.toLowerCase() === company : true;
        return matchesQuery && matchesCompany;
      });
    }
  
    onMount(fetchJobListings);
</script>
  <Navbar />

<main class="container">
    <h1>채용 공고 리스트</h1>
    <div class="search-filter">
        <input type="text" placeholder="검색어 입력" bind:value={searchQuery} on:input={filterJobs} />
        <select bind:value={filterCompany} on:change={filterJobs}>
        <option value="">모든 회사</option>
        {#each [...new Set(jobListings.map(job => job.company))] as company}
            <option value={company}>{company}</option>
        {/each}
        </select>
    </div>
    {#if error}
        <p class="error">{error}</p>
    {:else}
        <ul class="job-list">
        {#each filteredJobListings as job}
            <li class="job-item" on:click={() => window.location.hash = `/job/${job.id}`}>
            <h2>{job.title}</h2>
            <p><strong>회사:</strong> {job.company}</p>
            <p><strong>설명:</strong> {job.description}</p>
            </li>
        {/each}
        </ul>
    {/if}
</main>
  
  <style>
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      font-family: 'LotteMartDream', sans-serif;
    }
  
    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }
  
    .search-filter {
      display: flex;
      justify-content: space-between;
      margin-bottom: 20px;
    }
  
    .search-filter input,
    .search-filter select {
      padding: 10px;
      font-size: 1rem;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
  
    .search-filter select {
      width: 200px;
    }
  
    .error {
      color: red;
      text-align: center;
    }
  
    .job-list {
      list-style-type: none;
      padding: 0;
    }
  
    .job-item {
      background: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
      transition: background 0.3s, box-shadow 0.3s;
      cursor: pointer;
    }
  
    .job-item:hover {
      background: #f1f1f1;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
  
    h2 {
      margin-top: 0;
      color: #007BFF;
    }
  
    p {
      margin: 5px 0;
      color: #555;
    }
  
    p strong {
      color: #333;
    }
  </style>
  