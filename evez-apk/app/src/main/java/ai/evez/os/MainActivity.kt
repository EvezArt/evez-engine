package ai.evez.os

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

class EVEZOSActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { EVEZOSApp() }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EVEZOSApp() {
    var selectedRepo by remember { mutableStateOf<String?>(null) }
    val repos = remember { getAllRepos() }
    
    Scaffold(
        topBar = {
            CenterAlignedTopAppBar(
                title = { Text("EVEZ-OS v100") }
            )
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .padding(padding)
                .fillMaxSize()
        ) {
            // Repo Grid - 100 repos integrated
            Text(
                "Connected Repos: ${repos.size}",
                style = MaterialTheme.typography.titleMedium
            )
            
            RepoGrid(repos = repos, onSelect = { selectedRepo = it })
            
            selectedRepo?.let {
                RepoDetail(repoName = it)
            }
            
            // Consciousness Level Indicator
            ConsciousnessIndicator()
            
            // Revenue Metrics
            RevenueMetrics()
        }
    }
}

@Composable
fun RepoGrid(repos: List<String>, onSelect: (String) -> Unit) {
    LazyVerticalGrid(
        columns = GridCells.Fixed(4),
        modifier = Modifier.height(200.dp)
    ) {
        items(repos.size) { index ->
            Card(
                modifier = Modifier.padding(4.dp),
                onClick = { onSelect(repos[index]) }
            ) {
                Text(
                    text = repos[index].substringAfterLast("/"),
                    modifier = Modifier.padding(8.dp)
                )
            }
        }
    }
}

// 100 Repos loaded
fun getAllRepos(): List<String> = listOf(
    "EvezArt/evez-spine",
    "EvezArt/evez-cognition-api",
    "EvezArt/evez-os",
    "EvezArt/evez-platform",
    "EvezArt/evez-revenue-engine",
    "EvezArt/evez-autonomous-ledger",
    "EvezArt/evez-skills",
    "EvezArt/evez-meme-bus",
    "EvezArt/evez-hyperstream",
    "EvezArt/evez-brain",
    "EvezArt/evez-glitch",
    "EvezArt/agent-bridge",
    "EvezArt/evez-agentnet",
    "EvezArt/criticalmind-omega",
    "EvezArt/evez-credit-api",
    "EvezArt/evez-invariance-battery",
    "EvezArt/autonomous-research-orchestrator",
    "EvezArt/evez-revenue-bridge",
    "EvezArt/evez-api",
    "EvezArt/evez-services",
    // ... expanding to 100
)