<template>
  <!-- 模版里的代码只能有一个div -->
  <div>
    <div>
      <div class="header">
        <h1>title</h1>
        <img src="../assets/admin.jpg" alt />
      </div>

      <hr />

      <div class="content">
        <div class="menu">
          <div
            class="item"
            style="background: #777; color: #fff;"
          >
            <a>test1</a>
          </div>
        </div>

        <div class="userlist">
          <p>test2</p>
          <hr />

          <div class="user">
            <img src="/static/admin.jpg" alt />
            <p>test3</p>
          </div>
        </div>
      </div>
    </div>

    <hr />

    <div class="foot">
      <input type="text" style="height: 30ox; width: 700px;" />
      <p>[[inputText]]</p>Copyright © 2020 KeithSnow
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
};
</script>

<style>
  
</style>
