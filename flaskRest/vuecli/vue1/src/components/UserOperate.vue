<template>
  <div>
    <div class="form-group row">
      <label for="username">用户姓名</label>
      <input type="text" name="username" id="username" class="form-control" placeholder="请输入用户姓名">
    </div>
    <div class="form-group row">
      <label for="userage">用户年龄</label>
      <input type="number" name="userage" id="userage" class="form-control" placeholder="请输入用户年龄">
    </div>
    <div id="btns">
        <button type="button" class="btn btn-success" v-on:click="adduser">添加</button>
        <button type="button" class="btn btn-success" v-on:click="updateuser">更新</button>
        <button type="button" class="btn btn-success" v-on:click="deleteuser">删除</button>
        <button type="button" class="btn btn-success" v-on:click="getuser">查询</button>
    </div>
  </div>
</template>