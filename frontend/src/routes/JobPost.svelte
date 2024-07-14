<script>
  import { push } from 'svelte-spa-router'
  import Error from "../components/Error.svelte"

  let error = {detail:[]}
  let subject = ''
  let content = ''

  function post_question(event) {
      event.preventDefault()
      let url = ""
      let params = {
          subject: subject,
          content: content,
      }
      // fastapi('post', url, params, 
      //     (json) => {
      //         push("/")
      //     },
      //     (json_error) => {
      //         error = json_error
      //     }
      // )

  }
</script>

<style></style>

<div class="container">
  <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
  <Error error={error} />
  <form method="post" class="my-3">
      <div class="mb-3">
          <label for="subject">제목</label>
          <input type="text" class="form-control" bind:value="{subject}">
      </div>
      <div class="mb-3">
          <label for="content">내용</label>
          <textarea class="form-control" rows="10" bind:value="{content}"></textarea>
      </div>
      <button class="btn btn-primary" on:click="{post_question}">저장하기</button>
  </form>
</div>