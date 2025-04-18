import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  TextField,
  Button,
  List,
  ListItem,
  ListItemText,
  Grid,
  Box,
  Alert
} from "@mui/material";

const App = () => {
  // Stati per gestire il form e la lista delle missioni
  const [missions, setMissions] = useState([]);
  const [missionName, setMissionName] = useState("");
  const [missionDescription, setMissionDescription] = useState("");
  const [missionDate, setMissionDate] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  // Funzione per caricare le missioni esistenti
  const fetchMissions = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://localhost:8000/api/missions");
      setMissions(response.data);
    } catch (err) {
      setError("Failed to fetch missions.");
    } finally {
      setLoading(false);
    }
  };

  // Funzione per aggiungere una nuova missione
  const handleSubmit = async (e) => {
    e.preventDefault();
    const missionData = {
      name: missionName,
      description: missionDescription,
      date: missionDate,
    };

    try {
      const response = await axios.post("http://localhost:8000/api/missions", missionData);
      setSuccess(true);
      setMissionName("");
      setMissionDescription("");
      setMissionDate("");
      fetchMissions(); // Ricarica le missioni dopo l'aggiunta
    } catch (err) {
      setError("Failed to add mission.");
    }
  };

  // Effetto per caricare le missioni all'inizio
  useEffect(() => {
    fetchMissions();
  }, []);

  return (
    <Container maxWidth="md">
      <Typography variant="h4" gutterBottom align="center">
        Space Mission Simulator
      </Typography>

      {/* Form per aggiungere missione */}
      <Box component="form" onSubmit={handleSubmit} sx={{ mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          Add New Mission
        </Typography>
        <TextField
          fullWidth
          label="Mission Name"
          variant="outlined"
          value={missionName}
          onChange={(e) => setMissionName(e.target.value)}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Mission Description"
          variant="outlined"
          value={missionDescription}
          onChange={(e) => setMissionDescription(e.target.value)}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Mission Date"
          type="date"
          variant="outlined"
          value={missionDate}
          onChange={(e) => setMissionDate(e.target.value)}
          margin="normal"
          InputLabelProps={{
            shrink: true,
          }}
        />
        <Box sx={{ textAlign: "center" }}>
          <Button
            variant="contained"
            color="primary"
            type="submit"
            sx={{ mt: 2 }}
          >
            Add Mission
          </Button>
        </Box>
      </Box>

      {/* Messaggio di successo o errore */}
      {success && (
        <Alert severity="success" sx={{ mb: 2 }}>
          Mission added successfully!
        </Alert>
      )}
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {/* Lista delle missioni */}
      <Typography variant="h6" gutterBottom>
        Mission List
      </Typography>
      {loading ? (
        <Typography variant="body1">Loading missions...</Typography>
      ) : (
        <List>
          {missions.map((mission) => (
            <ListItem key={mission.id}>
              <ListItemText
                primary={mission.name}
                secondary={`Description: ${mission.description} | Date: ${mission.date}`}
              />
            </ListItem>
          ))}
        </List>
      )}
    </Container>
  );
};

export default App;
