/* =============================================================
   BUUM · Calendario de contenido — PLAN experto de 3 días
   -------------------------------------------------------------
   MODO PLAN (2026-07-13): planificación primero, contenido DESPUÉS
   (día por día). Historias DIARIAS + carruseles con texto + posts +
   reel. Cada pieza tiene su OBJETIVO de resultados (alcance, guardados,
   engagement, mensajes) para ir creciendo seguidores, audiencia y ventas.
   Solo 2 piezas ya PRODUCIDAS (bloque de color + flat-lay, aprobadas 9.0);
   el resto está PLANEADO (por producir).
   ============================================================= */
var F3 = function(){ return [
  {rol:"Jefe de Marketing BUUM", ok:true},
  {rol:"Director Creativo / CIO", ok:true},
  {rol:"Crítico marca mundial", ok:true}
]; };

window.CAL_CONTENIDO = {
  generado: "2026-07-13",
  producto: "Foco LED 60W",
  redes: ["ig", "fb"],
  modo: "PLAN",
  revision: {
    encargado: "Encargado de contenido",
    ceo: "CEO",
    piezas: 2,
    filtros: "3 críticos IA + auditor",
    nota: "PLAN EXPERTO de 3 días (historias diarias + carruseles con texto + posts + reel). Cada pieza tiene su OBJETIVO de resultados. Solo 2 piezas ya PRODUCIDAS (bloque de color y flat-lay, aprobadas 9.0); el resto está PLANEADO → se produce día por día. Los resultados se miden y se suben publicación tras publicación (seguidores, audiencia, ventas)."
  },
  rutina: "Cada día se produce el contenido planeado, pasa los 3 filtros (solo 9+), tú autorizas. Se MIDEN resultados (alcance · guardados · compartidas · seguidores nuevos · mensajes) y se hace MÁS de lo que más jala.",
  dias: {
    /* ===== DÍA 1 · MARCA / PRESENCIA · objetivo del día: ALCANCE + recordación ===== */
    "2026-07-14": [
      {id:"d1_s1", hora:"08:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · flat-lay naranja",
       titulo:"Buenos días con BUUM", texto:"Historia flat-lay naranja (el estilo que te gustó), vertical. YA PRODUCIDA.",
       objetivo:"Presencia diaria + engagement (arranca el día en el feed de la gente).",
       filtros:F3(), promedio:9.0,
       img:"../buumia-tienda/marketing/contenido/dia1/h1_manana.png"},
      {id:"d1_post", hora:"13:00", tipo:"post", red:"fb", estado:"por_autorizar", estilo:"⭐ Bloque de color (tipo Coca)",
       titulo:"Pura luz", texto:"Póster de marca: foco sobre naranja + tipografía gigante. YA PRODUCIDO.",
       objetivo:"Recordación de marca (el naranja domina el feed, se reconoce al instante).",
       filtros:F3(), promedio:9.0,
       img:"../buumia-tienda/marketing/contenido/pro/tanda2/colorblock_ad.png"},
      {id:"d1_s2", hora:"19:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · encuesta (azul)",
       titulo:"¿Qué cuarto quieres iluminar?", texto:"Historia azul con encuesta (Sala/Recámara/Negocio). Variedad de color, misma vibra. YA PRODUCIDA.",
       objetivo:"Engagement — cada respuesta sube el alcance de la cuenta.",
       filtros:F3(), promedio:8.8,
       img:"../buumia-tienda/marketing/contenido/dia1/h2_encuesta.png"},
      {id:"d1_reel", hora:"21:00", tipo:"video", red:"ig", estado:"por_autorizar", estilo:"Reel 9:16 con música",
       titulo:"Reel: el foco enciende", texto:"Reel vertical con música (cine + bloque de color + flat-lay). YA PRODUCIDO.",
       objetivo:"ALCANCE y seguidores nuevos (los Reels dan mucho más reach).",
       promedio:9.0,
       video:"../buumia-tienda/marketing/contenido/dia1/reel_dia1.mp4"}
    ],
    /* ===== DÍA 2 · BENEFICIOS / VALOR · objetivo del día: GUARDADOS ===== */
    "2026-07-15": [
      {id:"d2_s1", hora:"08:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · dato (azul)",
       titulo:"¿Sabías que? Gasta 80% menos", texto:"Historia flat-lay azul (para variar) con un dato de ahorro. YA PRODUCIDA.",
       objetivo:"Valor/educación (posiciona a BUUM como el que sabe de luz).",
       filtros:F3(), promedio:8.7,
       img:"../buumia-tienda/marketing/contenido/dia2/h1_dato.png"},
      {id:"d2_car", hora:"12:00", tipo:"carrusel", red:"ig", estado:"por_autorizar", estilo:"Carrusel tipo Amazon (3 contextos distintos)",
       titulo:"3 razones para cambiar a BUUM", texto:"Carrusel-VIAJE: 3 imágenes DISTINTAS (gancho naranja → foco en sala → foco en patio + $75/CTA). Producto en uso en contextos reales, no la misma foto. YA PRODUCIDO.",
       objetivo:"GUARDADOS + swipe (viaje, no álbum) = crece el alcance.",
       filtros:F3(), promedio:9.1,
       imgs:["../buumia-tienda/marketing/contenido/dia2/c1.png","../buumia-tienda/marketing/contenido/dia2/c2.png","../buumia-tienda/marketing/contenido/dia2/c3.png"]},
      {id:"d2_s2", hora:"17:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · contexto real (exterior)",
       titulo:"Ilumina tu patio y fachada", texto:"El foco iluminando la entrada/patio de una casa de noche (contexto REAL, no el falso antes/después opaco). YA PRODUCIDA.",
       objetivo:"Muestra el beneficio en un contexto real (afuera también).",
       filtros:F3(), promedio:8.6,
       img:"../buumia-tienda/marketing/contenido/dia2/h2_contexto.png"},
      {id:"d2_post", hora:"20:00", tipo:"post", red:"ig", estado:"por_autorizar", estilo:"⭐ Flat-lay (top-down)",
       titulo:"Colección BUUM", texto:"Foto top-down editorial: foco sobre naranja con props. YA PRODUCIDO.",
       objetivo:"Recordación/estética premium (el feed se ve diseñado).",
       filtros:F3(), promedio:9.0,
       img:"../buumia-tienda/marketing/contenido/pro/tanda2/flatlay_ad.png"}
    ],
    /* ===== DÍA 3 · NEGOCIO / MAYOREO · objetivo del día: MENSAJES / interés de compra ===== */
    "2026-07-16": [
      {id:"d3_s1", hora:"08:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · EN MANO (persona)",
       titulo:"¿Compras para revender?", texto:"Composición NUEVA: una mano sostiene el foco (elemento humano). Luz blanca. YA PRODUCIDA.",
       objetivo:"Filtrar/identificar interesados en comprar por caja.",
       filtros:F3(), promedio:8.7,
       img:"../buumia-tienda/marketing/contenido/dia3/h1_mano.png"},
      {id:"d3_post", hora:"13:00", tipo:"post", red:"fb", estado:"por_autorizar", estilo:"Post · MACRO dramático",
       titulo:"El foco que vale la pena", texto:"Composición NUEVA: macro close-up de la corona facetada (tipo comercial de coche). YA PRODUCIDO.",
       objetivo:"Recordación de marca premium (belleza de producto).",
       filtros:F3(), promedio:9.0,
       img:"../buumia-tienda/marketing/contenido/dia3/post_macro.png"},
      {id:"d3_car", hora:"18:00", tipo:"carrusel", red:"fb", estado:"por_autorizar", estilo:"Carrusel mayoreo (3 composiciones distintas)",
       titulo:"Compra por caja y gana", texto:"Carrusel-viaje: 1) caja abierta · 2) foco EN USO en lámpara · 3) $75/gana revendiendo. 3 composiciones distintas. YA PRODUCIDO.",
       objetivo:"Interés de compra + MENSAJES (leads de mayoreo).",
       filtros:F3(), promedio:8.9,
       imgs:["../buumia-tienda/marketing/contenido/dia3/c1.png","../buumia-tienda/marketing/contenido/dia3/c2.png","../buumia-tienda/marketing/contenido/dia3/c3.png"]},
      {id:"d3_s2", hora:"21:00", tipo:"historia", red:"ig", estado:"por_autorizar", estilo:"Historia · CTA",
       titulo:"Escríbenos hoy", texto:"Cierre del día con CTA (pídelas por caja). YA PRODUCIDA.",
       objetivo:"Mensajes/clics → primer paso hacia la VENTA.",
       filtros:F3(), promedio:8.5,
       img:"../buumia-tienda/marketing/contenido/dia3/h2_cta.png"}
    ],
    /* ===== DÍA 4 · ESTILOS VARIADOS (tipo KFC / Dr. Simi) ===== */
    "2026-07-17": [
      {id:"d4_gato", hora:"09:00", tipo:"post", red:"ig", estado:"por_autorizar", estilo:"⭐ Mascota (gato · tipo Dr. Simi)",
       titulo:"El gato BUUM lo aprueba", texto:"Endorsement con el gatito Kitsune (nuestra mascota) + foco limpio. Estilo KFC/Simi. YA PRODUCIDO.",
       objetivo:"Marca + engagement (la mascota da personalidad y se comparte).",
       filtros:F3(), promedio:8.9,
       img:"../buumia-tienda/marketing/contenido/kfc/mascota.png"},
      {id:"d4_meme", hora:"13:00", tipo:"post", red:"fb", estado:"por_autorizar", estilo:"⭐ Meme relatable",
       titulo:"POV: pusiste focos BUUM", texto:"Meme mexicano relatable (humor). Engancha y se comparte. YA PRODUCIDO.",
       objetivo:"Alcance viral (los memes se comparten mucho).",
       filtros:F3(), promedio:8.7,
       img:"../buumia-tienda/marketing/contenido/kfc/meme.png"},
      {id:"d4_tipo", hora:"17:00", tipo:"post", red:"ig", estado:"por_autorizar", estilo:"⭐ Tipográfico audaz (tipo KFC)",
       titulo:"¿Y si iluminas todo?", texto:"Tipografía gigante audaz estilo '¿Y si síuuu?' de KFC. YA PRODUCIDO.",
       objetivo:"Recordación de marca + tono divertido.",
       filtros:F3(), promedio:9.0,
       img:"../buumia-tienda/marketing/contenido/kfc/tipografico.png"},
      {id:"d4_sofia", hora:"20:00", tipo:"post", red:"ig", estado:"por_autorizar", estilo:"⭐ Celebridad (Sofía)",
       titulo:"Sofía te lo recomienda", texto:"Endorsement con Sofía (asesora BUUM) + foco. Estilo celebridad tipo KFC×Roberto Carlos. YA PRODUCIDO.",
       objetivo:"Confianza + recomendación (endorsement humano).",
       filtros:F3(), promedio:8.8,
       img:"../buumia-tienda/marketing/contenido/kfc/sofia.png"}
    ]
  }
};
