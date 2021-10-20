<script>
  let news = [];
  let url = "https://people.onliner.by/feed";
  let channelName = "";

  async function getNews() {
    news = await (
      await fetch(`http://localhost:3000/news/?source=${url}`)
    ).json();
    url = "";
    channelName = news[0].channel_title;
  }
</script>

<main>
  <div class="feed">
    <div class="centered">
      <input bind:value={url} />
      <button on:click={getNews} class="submit"> Fetch news </button>
      <h1>{channelName}</h1>
    </div>
    {#each news as item}
      <div class="news">
        <h2>{item.title}</h2>
        <p>{item.description}</p>
        <a href={item.link}>Read more</a>
        <img src={item.image} alt="Loading" />
      </div>
    {/each}
  </div>
</main>

<style>
  div.news {
    margin-top: 5%;
    background-color: #2e3440;
    color: #eceff4;
    padding: 2%;
    border: 4px solid #4c566a;
  }
  a {
    color: #a3be8c;
  }
  img {
    margin-left: auto;
    margin-right: auto;
    display: block;
  }
  div.centered {
    text-align: center;
  }
  input {
    width: 75%;
    background-color: #4c566a;
    color: #eceff4;
    border: #eceff4 solid;
  }
  button.submit {
    width: 20%;
    padding: 1px;
    background: #4c566a;
    color: #ebcb8b;
    border: #eceff4 solid;
  }
  h1 {
    color: #ebcb8b;
    font-weight: bold;
  }
  h2 {
    font-weight: bold;
    color: #88c0d0;
  }
  :global(body) {
    font-family: monospace;
    background-color: #2e3440;
    color: #eceff4;
  }
  div.feed {
    margin-left: auto;
    margin-right: auto;
    width: 50%;
  }
</style>
