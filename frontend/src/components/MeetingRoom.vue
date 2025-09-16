<template>
  <div class="meeting-container">
    <el-select v-model="formData.roomId" placeholder="请选择会议室" class="room-select">
      <el-option-group
        v-for="group in roomGroups"
        :key="group.label"
        :label="group.label"
      >
        <el-option
          v-for="room in group.options"
          :key="room.id"
          :label="room.name"
          :value="room.id"
        />
      </el-option-group>
    </el-select>

    <el-date-picker
      v-model="formData.startTime"
      type="datetime"
      placeholder="选择开始时间"
      value-format="YYYY-MM-DD HH:mm:ss"
      class="time-picker"
    />

    <el-date-picker
      v-model="formData.endTime"
      type="datetime"
      placeholder="选择结束时间"
      value-format="YYYY-MM-DD HH:mm:ss"
      class="time-picker"
    />

    <el-button 
      type="primary" 
      @click="handleTrigger"
      :loading="isLoading"
      class="trigger-btn"
    >
      立即触发会议
    </el-button>
    
    <div class="status-display">
      <el-alert
        :title="statusMessage"
        :type="statusType"
        :closable="false"
        show-icon
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const selectedRoom = ref('')
const isLoading = ref(false)
const statusMessage = ref('等待操作')
const statusType = ref('info')

const roomGroups = ref([
  {
    label: '北京会议室',
    options: [
      { id: 262, name: '颐和园' },
      { id: 263, name: '奥森' },
      { id: 15979, name: '五根松' },
      { id: 260, name: '水立方' }
    ]
  },
  {
    label: '成都会议室',
    options: [
      { id: 941, name: '丽江' },
      { id: 2090, name: '海南岛' },
      { id: 2091, name: '东极岛' },
      { id: 2099, name: '钓鱼岛' }
    ]
  }
])

const formData = ref({
  roomId: '',
  startTime: '',
  endTime: '',
  userId: 2486181
})

const handleTrigger = async () => {
  try {
    if (!formData.value.endTime || !formData.value.startTime) {
      throw new Error('请选择完整的时间范围')
    }
    
    const params = {
      ...formData.value,
      startTime: new Date(formData.value.startTime).getTime(),
      endTime: new Date(formData.value.endTime).getTime()
    }

    const response = await axios.post('http://localhost:5000/api/trigger-meeting', params)
    isLoading.value = true
    statusMessage.value = '请求处理中...'
    
    const response = await axios.post('http://localhost:5000/trigger-meeting', {
      roomId: selectedRoom.value
    })
    
    statusType.value = response.data.status === 'success' ? 'success' : 'error'
    statusMessage.value = response.data.status === 'success' 
      ? '会议创建成功' 
      : '会议创建失败'
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = `请求异常: ${error.message}`
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.meeting-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 20px;
  background: var(--el-bg-color);
  border-radius: 8px;
  box-shadow: var(--el-box-shadow-light);
}

.room-select {
  width: 100%;
  margin-bottom: 1.5rem;
}

.trigger-btn {
  width: 100%;
  margin-bottom: 1.5rem;
}

.status-display {
  margin-top: 1rem;
}
</style>