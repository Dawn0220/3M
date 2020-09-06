<template>
  <div class="my_task" style="font-family: 'jdjszhong'; font-weight: bold; display:block;">
    <!-- <div class="dashboard-text">name: {{ name }}</div> -->
    <h1> My Release </h1>
    <div class="box" style="font-family: 'jdjszhong'; font-weight: bold; display:block;">
      <el-row>
        <el-col :span="3"> <p> Title </p> </el-col>
        <el-col :span="7"> <p> Position </p> </el-col>
        <el-col :span="3"> <p> Participants </p> </el-col>
        <el-col :span="3"> <p> Keywords </p> </el-col>
        <el-col :span="2" class="class"> <p> State </p> </el-col>
        <el-col :span="6"> <p> Operation </p>  </el-col>
      </el-row>
    </div>
    <div
      v-for="activity in activities"
      :key="activity.title"
      class='box row' >
        <div>
          <el-row>
            <el-col :span="3"> <p> {{ activity.title }} </p> </el-col>
            <el-col :span="7"> <p> {{ activity.position }} </p> </el-col>
            <el-col :span="3"> <p> {{ activity.participant }} </p> </el-col>
            <el-col :span="3"> <p> {{ activity.key_word }} </p> </el-col>
            <el-col :span="2">
              <el-tag :type="activity.status | statusFilter" class='tag'>{{ activity.status }}</el-tag>
            </el-col>

            <el-col :span="2"> <el-button type="primary" @click="drawer = true" style="font-family: 'jdjszhong'; display:block;">Chat</el-button>  </el-col>
            <el-col :span="2"> <el-button type="success" @click="drawer = true" style="font-family: 'jdjszhong'; display:block; position: relative; left: -5px"">Accept</el-button>  </el-col>
            <el-col :span="2"> <el-button type="warning" @click="drawer = true" style="font-family: 'jdjszhong'; display:block;">Reject</el-button> </el-col>
          </el-row>
        </div>
        <el-drawer
          title=""
          :visible.sync="drawer"
          :direction="direction"
          :before-close="handleClose"
          >
          <div class="chat">
            <img src="../../assets/chat.png" class="chat_pic" />
            <div class="input">
              <el-row gutter="20">
              <el-col :span="4"> <img src="../../assets/user_log.jpg" class="user_pic" /> </el-col>
              <el-col :span="16"> <el-input v-model="input" placeholder="请输入内容"></el-input> </el-col>
              <el-col :span="4"> <el-button type="primary" style="font-family: 'jdjszhong'; font-weight: bold; display:block;">Send</el-button> </el-col>
              </el-row>
            </div>
          </div>
        </el-drawer>
    </div>

  </div>
</template>

<script>
// import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  filters: {
    statusFilter(status) {
      const statusMap = {
        finished: 'success',
        in_progress: 'gray',
        cancel: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      activities: [
        {title: '-', position: '-', status: '-', participant: '', key_word: ''},
      ],
      drawer: false
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      this.axios
        .post('/get_released_task', {
          user_id: 'admin'
        })
        .then((res) => {
          this.activities = res.data["data"]
        })
        .catch((error) => {
          alert(error)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.my_task{
  margin: 40px;
}
.box{
  // border-radius: 10%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  padding: 20px;
  margin: 20px 0px;
}

.box{
  .title{
    font-weight:bold;
  }
}
.tag{
  size: 60px;
  margin-top: 6px;
  margin-left: -38px;
}
.user_pic{
  height: 40px;
}
.chat_pic{
  height: 700px;
}
.chat{
  margin: 0px 40px;
}
</style>
