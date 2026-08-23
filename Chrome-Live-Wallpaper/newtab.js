const input = document.getElementById("wallpaperInput");
const wallpaper = document.getElementById("wallpaper");
function render(dataUrl, type) {
  wallpaper.innerHTML = type.startsWith("video")
    ? `<video src="${dataUrl}" autoplay muted loop></video>`
    : `<img src="${dataUrl}">`;
}
chrome.storage.local.get(["wallpaperData", "wallpaperType"], (res) => {
  if (res.wallpaperData) render(res.wallpaperData, res.wallpaperType);
});
input.addEventListener("change", () => {
  const file = input.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    chrome.storage.local.set({ wallpaperData: reader.result, wallpaperType: file.type });
    render(reader.result, file.type);
  };
  reader.readAsDataURL(file);
});
const removeBtn = document.getElementById("removeBtn");
removeBtn.addEventListener("click", () => {
  chrome.storage.local.remove(["wallpaperData", "wallpaperType"]);
  wallpaper.innerHTML = "";
});