// EVEZ-OS Revenue UI Connection
// Auto-generated from schema

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useState } from 'react'

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:9111/api'

// Types from schema
interface Agent {
  id: number
  uuid: string
  name: string
  mission?: string
  status: 'idle' | 'running' | 'paused' | 'error' | 'terminated'
  agentType: 'executor' | 'skeptic' | 'architect' | 'explorer' | 'evolver' | 'meta' | 'aegis' | 'watchdog'
  recursionDepth: number
  parentAgentId?: number
  phi: number
  healthScore: number
  longeviate: boolean
  config?: any
}

interface AgentTask {
  id: number
  uuid: string
  sourceSystem: string
  targetSystem?: string
  requestedAction: string
  payload?: any
  status: 'pending' | 'assigned' | 'running' | 'success' | 'failed' | 'retrying'
  priority: number
  agentId?: number
  result?: any
  errorLog?: string
  callbackUrl?: string
  decayFactor: number
  thresholdValue: number
  fireCount: number
}

interface RevenueEvent {
  id: number
  uuid: string
  fireId?: string
  source: string
  amount: number
  currency: string
  status: 'pending' | 'confirmed' | 'failed' | 'refunded'
  stripeEventId?: string
  metadata?: any
}

// Hooks
export const useAgents = () => {
  return useQuery<Agent[]>({
    queryKey: ['agents'],
    queryFn: async () => {
      const res = await fetch(`${API_BASE}/agents`)
      if (!res.ok) throw new Error('Failed to fetch agents')
      return res.json()
    },
    refetchInterval: 5000, // Real-time updates
  })
}

export const useAgentTasks = () => {
  return useQuery<AgentTask[]>({
    queryKey: ['agent-tasks'],
    queryFn: async () => {
      const res = await fetch(`${API_BASE}/agent-tasks`)
      if (!res.ok) throw new Error('Failed to fetch tasks')
      return res.json()
    },
    refetchInterval: 3000,
  })
}

export const useRevenueEvents = () => {
  return useQuery<RevenueEvent[]>({
    queryKey: ['revenue-events'],
    queryFn: async () => {
      const res = await fetch(`${API_BASE}/revenue-events`)
      if (!res.ok) throw new Error('Failed to fetch revenue')
      return res.json()
    },
  })
}

export const useHealthScore = () => {
  return useQuery<{ healthScore: number; phi: number; activeAgents: number }>({
    queryKey: ['health'],
    queryFn: async () => {
      const res = await fetch(`${API_BASE}/health`)
      if (!res.ok) throw new Error('Failed to fetch health')
      return res.json()
    },
    refetchInterval: 2000,
  })
}

// Components
export const AgentDashboard = () => {
  const { data: agents, isLoading } = useAgents()
  const { data: tasks } = useAgentTasks()
  const { data: health } = useHealthScore()

  if (isLoading) return <div>Loading agents...</div>

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">EVEZ-OS Command Center</h1>
      
      <div className="grid grid-cols-3 gap-4 mb-6">
        <div className="bg-blue-100 p-4 rounded">
          <h3 className="font-bold">Health Score</h3>
          <p className="text-3xl">{health?.healthScore?.toFixed(2)}</p>
        </div>
        <div className="bg-green-100 p-4 rounded">
          <h3 className="font-bold">Φ</h3>
          <p className="text-3xl">{health?.phi?.toFixed(3)}</p>
        </div>
        <div className="bg-purple-100 p-4 rounded">
          <h3 className="font-bold">Active Agents</h3>
          <p className="text-3xl">{health?.activeAgents}</p>
        </div>
      </div>

      <h2 className="text-xl font-bold mb-2">Agents</h2>
      <div className="grid grid-cols-2 gap-4">
        {agents?.map(agent => (
          <div key={agent.id} className="border p-3 rounded">
            <h3 className="font-bold">{agent.name}</h3>
            <p>Status: {agent.status}</p>
            <p>Health: {(agent.healthScore * 100).toFixed(0)}%</p>
            <p>Φ: {agent.phi.toFixed(3)}</p>
          </div>
        ))}
      </div>

      <h2 className="text-xl font-bold mt-6 mb-2">Task Queue</h2>
      <div className="max-h-60 overflow-y-auto">
        {tasks?.map(task => (
          <div key={task.id} className="border-b py-2">
            <span className={`px-2 py-1 rounded text-xs ${
              task.status === 'success' ? 'bg-green-200' :
              task.status === 'running' ? 'bg-yellow-200' :
              task.status === 'failed' ? 'bg-red-200' : 'bg-gray-200'
            }`}>
              {task.status}
            </span>
            <span className="ml-3">{task.requestedAction}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

export default AgentDashboard