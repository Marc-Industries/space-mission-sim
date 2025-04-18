const API_URL = import.meta.env.VITE_API_URL;

export const getMissions = async () => {
  const res = await fetch(`${API_URL}/missions`);
  return res.json();
};

export const createMission = async (mission) => {
  const res = await fetch(`${API_URL}/missions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(mission),
  });
  return res.json();
};

export const updateMission = async (id, mission) => {
  const res = await fetch(`${API_URL}/missions/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(mission),
  });
  return res.json();
};

export const deleteMission = async (id) => {
  const res = await fetch(`${API_URL}/missions/${id}`, {
    method: "DELETE",
  });
  return res.json();
};
