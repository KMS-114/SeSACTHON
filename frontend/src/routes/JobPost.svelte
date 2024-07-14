<script>
    import { onMount } from 'svelte';
    let username = '';
    let age = '';
    let gender = 'male';
    let resultText = '';

    function submit() {
        resultText = `Username: ${username}<br>Age: ${age}<br>Gender: ${gender}`;
    }
</script>

<style>
    body { font-family: Arial, sans-serif; }
    .container { max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
    h1 { text-align: center; }
    label { display: block; margin-top: 10px; }
    input, select { width: 100%; padding: 8px; margin-top: 5px; }
    .result { margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; background-color: #f9f9f9; }
</style>

<div class="container">
    <h1>Input Form</h1>
    <label for="username">Username:</label>
    <input type="text" bind:value={username} id="username">
    
    <label for="age">Age:</label>
    <input type="number" bind:value={age} id="age">
    
    <label for="gender">Gender:</label>
    <select bind:value={gender} id="gender">
        <option value="male">Male</option>
        <option value="female">Female</option>
    </select>
    
    <button on:click={submit}>Submit</button>
    
    <div class="result" id="result" innerHTML={resultText}></div>
</div>
