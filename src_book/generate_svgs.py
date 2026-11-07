import math

def create_svg_cartesian():
    # 3D isometric representation of Cartesian Coordinates (x, y, z)
    # Origin at (180, 240)
    # x axis points down-left (cos 210°, sin 210°) -> (-0.866, 0.5)
    # y axis points right (cos 0°, sin 0°) -> (1, 0)
    # z axis points straight up -> (0, -1)
    svg = '''<svg width="600" height="380" viewBox="0 0 600 380" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#0284c7"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="300" y="30" text-anchor="middle" font-family="Times New Roman, serif" font-size="18" font-weight="bold" fill="#0f172a">Repère Cartésien 3D : R(O ; e_x, e_y, e_z)</text>

  <!-- Axes -->
  <!-- Origin O -->
  <!-- Axis X (down-left) -->
  <line x1="200" y1="240" x2="70" y2="315" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="55" y="325" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">x</text>

  <!-- Axis Y (right-down) -->
  <line x1="200" y1="240" x2="480" y2="240" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="495" y="245" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">y</text>

  <!-- Axis Z (up) -->
  <line x1="200" y1="240" x2="200" y2="60" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="195" y="50" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">z</text>

  <text x="185" y="255" font-family="Times New Roman, serif" font-size="15" font-style="italic" fill="#475569">O</text>

  <!-- Coordinates of M: x_0=100 (along x), y_0=180 (along y), z_0=120 (along z) -->
  <!-- Projecting point P_xy on xy plane: O + x_vec + y_vec -->
  <!-- x vector: dx = -100 * 0.866 = -86.6, dy = 100 * 0.5 = 50 -> (113.4, 290) -->
  <!-- y vector: dx = 180, dy = 0 -->
  <!-- P_x = (113, 290) -->
  <!-- P_y = (380, 240) -->
  <!-- P_xy = (113 + 180, 290) = (293, 290) -->
  <!-- Point M = P_xy + (0, -130) = (293, 160) -->
  <!-- P_z = (200, 110) -->

  <!-- Projections (dashed lines) -->
  <line x1="113" y1="290" x2="293" y2="290" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="380" y1="240" x2="293" y2="290" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="293" y1="290" x2="293" y2="160" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="200" y1="110" x2="293" y2="160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Volume element dtau box around M -->
  <polygon points="293,160 333,160 308,175 268,175" fill="#bae6fd" fill-opacity="0.6" stroke="#0284c7" stroke-width="1"/>
  <polygon points="268,175 308,175 308,205 268,205" fill="#7dd3fc" fill-opacity="0.6" stroke="#0284c7" stroke-width="1"/>
  <polygon points="308,175 333,160 333,190 308,205" fill="#38bdf8" fill-opacity="0.6" stroke="#0284c7" stroke-width="1"/>

  <!-- Position vector OM -->
  <line x1="200" y1="240" x2="293" y2="160" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arrow-red)"/>
  <circle cx="293" cy="160" r="4" fill="#dc2626"/>
  <text x="305" y="155" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#dc2626">M(x, y, z)</text>
  <text x="235" y="195" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#dc2626">r = OM</text>

  <!-- Unit basis vectors at O -->
  <line x1="200" y1="240" x2="160" y2="263" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <text x="145" y="280" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#0284c7">e_x</text>

  <line x1="200" y1="240" x2="250" y2="240" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <text x="245" y="230" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#0284c7">e_y</text>

  <line x1="200" y1="240" x2="200" y2="190" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <text x="208" y="200" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#0284c7">e_z</text>

  <!-- Annotations -->
  <rect x="360" y="65" width="220" height="135" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="370" y="88" font-family="Times New Roman, serif" font-size="13" font-weight="bold" fill="#0f172a">Éléments différentiels :</text>
  <text x="370" y="110" font-family="Times New Roman, serif" font-size="12" fill="#334155">• OM = x e_x + y e_y + z e_z</text>
  <text x="370" y="130" font-family="Times New Roman, serif" font-size="12" fill="#334155">• dOM = dx e_x + dy e_y + dz e_z</text>
  <text x="370" y="150" font-family="Times New Roman, serif" font-size="12" fill="#334155">• Volume : dτ = dx dy dz</text>
  <text x="370" y="170" font-family="Times New Roman, serif" font-size="12" fill="#334155">• Base orthonormée directe fixe</text>
  <text x="370" y="190" font-family="Times New Roman, serif" font-size="12" fill="#334155">• e_x ∧ e_y = e_z</text>
</svg>'''
    return svg

def create_svg_cylindrical():
    svg = '''<svg width="600" height="400" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="c-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <marker id="c-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#0284c7"/>
    </marker>
    <marker id="c-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
    <marker id="c-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#16a34a"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="300" y="30" text-anchor="middle" font-family="Times New Roman, serif" font-size="18" font-weight="bold" fill="#0f172a">Repère Cylindrique 3D : (r, θ, z ; e_r, e_θ, e_z)</text>

  <!-- Origin (220, 260) -->
  <!-- Base Ellipse for cylinder bottom -->
  <ellipse cx="220" cy="260" rx="140" ry="50" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Axes -->
  <line x1="220" y1="260" x2="100" y2="330" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#c-arr)"/>
  <text x="85" y="340" font-family="Times New Roman, serif" font-size="15" fill="#64748b">x</text>

  <line x1="220" y1="260" x2="420" y2="260" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#c-arr)"/>
  <text x="430" y="265" font-family="Times New Roman, serif" font-size="15" fill="#64748b">y</text>

  <line x1="220" y1="260" x2="220" y2="60" stroke="#1e293b" stroke-width="2" marker-end="url(#c-arr)"/>
  <text x="215" y="50" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">z</text>
  <text x="205" y="275" font-family="Times New Roman, serif" font-size="15" font-style="italic">O</text>

  <!-- Point H in xy-plane: angle theta=40 deg from x axis -->
  <!-- Vector in xy-plane: let H be at (320, 290) -->
  <line x1="220" y1="260" x2="320" y2="290" stroke="#0284c7" stroke-width="2"/>
  <circle cx="320" cy="290" r="3" fill="#0284c7"/>
  <text x="330" y="305" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0284c7">H (projeté)</text>
  <text x="270" y="290" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0284c7">r</text>

  <!-- Angle theta arc -->
  <path d="M 170,290 A 50,25 0 0,0 255,270" fill="none" stroke="#ea580c" stroke-width="2"/>
  <text x="225" y="305" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#ea580c">θ</text>

  <!-- Point M: H + (0, -150) = (320, 140) -->
  <line x1="320" y1="290" x2="320" y2="140" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="220" y1="140" x2="320" y2="140" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="320" cy="140" r="5" fill="#dc2626"/>
  <text x="335" y="135" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#dc2626">M(r, θ, z)</text>

  <!-- Vector OM -->
  <line x1="220" y1="260" x2="320" y2="140" stroke="#dc2626" stroke-width="2" marker-end="url(#c-red)"/>

  <!-- Local mobile basis vectors at M -->
  <!-- e_r (along HM direction) -->
  <line x1="320" y1="140" x2="370" y2="155" stroke="#16a34a" stroke-width="2.5" marker-end="url(#c-green)"/>
  <text x="380" y="165" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#16a34a">e_r</text>

  <!-- e_theta (tangent, perpendicular to e_r in horizontal plane) -->
  <line x1="320" y1="140" x2="295" y2="115" stroke="#ea580c" stroke-width="2.5" marker-end="url(#c-arr)"/>
  <text x="270" y="110" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#ea580c">e_θ</text>

  <!-- e_z (vertical upwards) -->
  <line x1="320" y1="140" x2="320" y2="90" stroke="#0284c7" stroke-width="2.5" marker-end="url(#c-blue)"/>
  <text x="325" y="85" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#0284c7">e_z</text>

  <!-- Box for Cylindrical Properties -->
  <rect x="370" y="240" width="215" height="145" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="380" y="260" font-family="Times New Roman, serif" font-size="13" font-weight="bold" fill="#0f172a">Formulaire Cylindrique :</text>
  <text x="380" y="280" font-family="Times New Roman, serif" font-size="12" fill="#334155">• x = r cos θ,  y = r sin θ,  z = z</text>
  <text x="380" y="300" font-family="Times New Roman, serif" font-size="12" fill="#334155">• OM = r e_r + z e_z</text>
  <text x="380" y="320" font-family="Times New Roman, serif" font-size="12" fill="#334155">• dOM = dr e_r + r dθ e_θ + dz e_z</text>
  <text x="380" y="340" font-family="Times New Roman, serif" font-size="12" fill="#334155">• Volume : dτ = r dr dθ dz</text>
  <text x="380" y="360" font-family="Times New Roman, serif" font-size="12" fill="#334155">• dS_lat = r dθ dz e_r</text>
</svg>'''
    return svg

def create_svg_spherical():
    svg = '''<svg width="600" height="420" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="s-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <marker id="s-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#0284c7"/>
    </marker>
    <marker id="s-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
    <marker id="s-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#16a34a"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="300" y="30" text-anchor="middle" font-family="Times New Roman, serif" font-size="18" font-weight="bold" fill="#0f172a">Repère Sphérique 3D : (r, θ, φ ; e_r, e_θ, e_φ)</text>

  <!-- Origin (220, 260) -->
  <!-- Sphere Outline & Equator -->
  <circle cx="220" cy="240" r="140" fill="none" stroke="#e2e8f0" stroke-width="1.5"/>
  <ellipse cx="220" cy="240" rx="140" ry="40" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Axes -->
  <line x1="220" y1="240" x2="100" y2="310" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#s-arr)"/>
  <text x="85" y="320" font-family="Times New Roman, serif" font-size="15" fill="#64748b">x</text>

  <line x1="220" y1="240" x2="420" y2="240" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#s-arr)"/>
  <text x="430" y="245" font-family="Times New Roman, serif" font-size="15" fill="#64748b">y</text>

  <line x1="220" y1="240" x2="220" y2="50" stroke="#1e293b" stroke-width="2" marker-end="url(#s-arr)"/>
  <text x="215" y="40" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">z</text>
  <text x="205" y="255" font-family="Times New Roman, serif" font-size="15" font-style="italic">O</text>

  <!-- Point M on Sphere surface: r = 140, theta=45 deg, phi=35 deg -->
  <!-- Position of M: (315, 140) -->
  <!-- Projection H on equator: (315, 260) -->
  <line x1="220" y1="240" x2="315" y2="260" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="315" y1="260" x2="315" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="315" cy="260" r="3" fill="#64748b"/>
  <text x="325" y="270" font-family="Times New Roman, serif" font-size="13" fill="#64748b">H</text>

  <!-- Vector OM -->
  <line x1="220" y1="240" x2="315" y2="140" stroke="#dc2626" stroke-width="2.5" marker-end="url(#s-red)"/>
  <circle cx="315" cy="140" r="5" fill="#dc2626"/>
  <text x="325" y="130" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#dc2626">M(r, θ, φ)</text>
  <text x="250" y="180" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">r = OM</text>

  <!-- Angle theta (colatitude, from Oz) -->
  <path d="M 220,170 A 70,70 0 0,1 260,198" fill="none" stroke="#7c3aed" stroke-width="2"/>
  <text x="245" y="165" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#7c3aed">θ (colatitude)</text>

  <!-- Angle phi (azimuth, from Ox in xy plane) -->
  <path d="M 180,265 A 50,20 0 0,0 260,250" fill="none" stroke="#ea580c" stroke-width="2"/>
  <text x="215" y="285" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#ea580c">φ (azimut)</text>

  <!-- Local mobile basis vectors at M -->
  <!-- e_r (radial outgoing) -->
  <line x1="315" y1="140" x2="365" y2="88" stroke="#dc2626" stroke-width="2.5" marker-end="url(#s-red)"/>
  <text x="370" y="85" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">e_r</text>

  <!-- e_theta (tangent to meridian, increasing theta) -->
  <line x1="315" y1="140" x2="360" y2="175" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#s-arr)"/>
  <text x="368" y="185" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#7c3aed">e_θ</text>

  <!-- e_phi (tangent to parallel, increasing phi) -->
  <line x1="315" y1="140" x2="280" y2="125" stroke="#ea580c" stroke-width="2.5" marker-end="url(#s-arr)"/>
  <text x="260" y="115" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#ea580c">e_φ</text>

  <!-- Box for Spherical Properties -->
  <rect x="375" y="250" width="215" height="155" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="385" y="270" font-family="Times New Roman, serif" font-size="13" font-weight="bold" fill="#0f172a">Formulaire Sphérique :</text>
  <text x="385" y="290" font-family="Times New Roman, serif" font-size="12" fill="#334155">• x = r sin θ cos φ</text>
  <text x="385" y="308" font-family="Times New Roman, serif" font-size="12" fill="#334155">• y = r sin θ sin φ</text>
  <text x="385" y="326" font-family="Times New Roman, serif" font-size="12" fill="#334155">• z = r cos θ</text>
  <text x="385" y="346" font-family="Times New Roman, serif" font-size="12" fill="#334155">• dOM = dr e_r + r dθ e_θ + r sinθ dφ e_φ</text>
  <text x="385" y="366" font-family="Times New Roman, serif" font-size="12" fill="#334155">• Volume : dτ = r² sin θ dr dθ dφ</text>
  <text x="385" y="386" font-family="Times New Roman, serif" font-size="12" fill="#334155">• dS_sphère = r² sin θ dθ dφ e_r</text>
</svg>'''
    return svg

def create_svg_symmetry():
    # Symmetry and Antisymmetry representation in 3D
    svg = '''<svg width="600" height="380" viewBox="0 0 600 380" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="sym-e" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#2563eb"/>
    </marker>
    <marker id="sym-b" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="300" y="28" text-anchor="middle" font-family="Times New Roman, serif" font-size="17" font-weight="bold" fill="#0f172a">Symétries et Antisymétries : Comportement de E (Polaire) et B (Axial)</text>

  <!-- Left: Plan de Symétrie Pi -->
  <g transform="translate(10, 45)">
    <!-- Plane Pi in 3D -->
    <polygon points="40,80 200,40 240,240 80,280" fill="#dbeafe" fill-opacity="0.6" stroke="#3b82f6" stroke-width="2"/>
    <text x="140" y="70" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1d4ed8">Plan de Symétrie Π</text>

    <!-- Point M on Plane -->
    <circle cx="150" cy="160" r="5" fill="#0f172a"/>
    <text x="135" y="180" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0f172a">M ∈ Π</text>

    <!-- Field E at M: Must BE IN THE PLANE -->
    <line x1="150" y1="160" x2="200" y2="120" stroke="#2563eb" stroke-width="3" marker-end="url(#sym-e)"/>
    <text x="210" y="125" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#2563eb">E(M) ∈ Π</text>

    <!-- Field B at M: Must BE ORTHOGONAL TO THE PLANE -->
    <line x1="150" y1="160" x2="90" y2="120" stroke="#dc2626" stroke-width="3" marker-end="url(#sym-b)"/>
    <text x="40" y="115" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">B(M) ⟂ Π</text>

    <!-- Subtitle card -->
    <rect x="25" y="285" width="230" height="40" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
    <text x="140" y="302" text-anchor="middle" font-family="Times New Roman, serif" font-size="12" font-weight="bold" fill="#1e40af">Si Π est plan de symétrie :</text>
    <text x="140" y="318" text-anchor="middle" font-family="Times New Roman, serif" font-size="12" fill="#1e3a8a">E(M) est DANS Π  |  B(M) est NORMAL à Π</text>
  </g>

  <!-- Right: Plan d'Antisymétrie Pi* -->
  <g transform="translate(310, 45)">
    <!-- Plane Pi* in 3D -->
    <polygon points="40,80 200,40 240,240 80,280" fill="#fee2e2" fill-opacity="0.6" stroke="#ef4444" stroke-width="2"/>
    <text x="120" y="70" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#b91c1c">Plan d'Antisymétrie Π*</text>

    <!-- Point M on Plane -->
    <circle cx="150" cy="160" r="5" fill="#0f172a"/>
    <text x="135" y="180" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0f172a">M ∈ Π*</text>

    <!-- Field E at M: Must BE ORTHOGONAL TO THE PLANE -->
    <line x1="150" y1="160" x2="90" y2="120" stroke="#2563eb" stroke-width="3" marker-end="url(#sym-e)"/>
    <text x="35" y="115" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#2563eb">E(M) ⟂ Π*</text>

    <!-- Field B at M: Must BE IN THE PLANE -->
    <line x1="150" y1="160" x2="200" y2="120" stroke="#dc2626" stroke-width="3" marker-end="url(#sym-b)"/>
    <text x="210" y="125" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">B(M) ∈ Π*</text>

    <!-- Subtitle card -->
    <rect x="25" y="285" width="230" height="40" rx="4" fill="#fef2f2" stroke="#fecaca"/>
    <text x="140" y="302" text-anchor="middle" font-family="Times New Roman, serif" font-size="12" font-weight="bold" fill="#991b1b">Si Π* est plan d'antisymétrie :</text>
    <text x="140" y="318" text-anchor="middle" font-family="Times New Roman, serif" font-size="12" fill="#7f1d1d">E(M) est NORMAL à Π* | B(M) est DANS Π*</text>
  </g>
</svg>'''
    return svg

def create_svg_gauss_cylinder():
    # 3D Gauss Surface (Cylinder) around infinite charged line / cylinder
    svg = '''<svg width="600" height="360" viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="g-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
    <marker id="g-n" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#0284c7"/>
    </marker>
  </defs>

  <text x="300" y="26" text-anchor="middle" font-family="Times New Roman, serif" font-size="17" font-weight="bold" fill="#0f172a">Application du Théorème de Gauss : Cylindre Fermé Σ</text>

  <!-- Central Charged Line Oz -->
  <line x1="300" y1="30" x2="300" y2="330" stroke="#dc2626" stroke-width="4"/>
  <text x="312" y="45" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">Axe Oz (Charge λ)</text>

  <!-- Gauss Cylinder -->
  <!-- Top Base -->
  <ellipse cx="300" cy="110" rx="120" ry="35" fill="#e0f2fe" fill-opacity="0.7" stroke="#0284c7" stroke-width="2"/>
  <text x="300" y="95" text-anchor="middle" font-family="Times New Roman, serif" font-size="13" font-weight="bold" fill="#0369a1">Base Supérieure S_sup : n ⟂ E ⇒ Flux = 0</text>

  <!-- Cylinder Lateral surface -->
  <path d="M 180,110 L 180,250 A 120,35 0 0,0 420,250 L 420,110" fill="#bae6fd" fill-opacity="0.3" stroke="#0284c7" stroke-width="2"/>

  <!-- Bottom Base -->
  <ellipse cx="300" cy="250" rx="120" ry="35" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 180,250 A 120,35 0 0,0 420,250" fill="none" stroke="#0284c7" stroke-width="2"/>
  <text x="300" y="300" text-anchor="middle" font-family="Times New Roman, serif" font-size="13" font-weight="bold" fill="#0369a1">Base Inférieure S_inf : n ⟂ E ⇒ Flux = 0</text>

  <!-- Normal vector and Field vector on lateral surface -->
  <!-- On right edge (420, 180) -->
  <line x1="420" y1="180" x2="480" y2="180" stroke="#0284c7" stroke-width="2.5" marker-end="url(#g-n)"/>
  <text x="485" y="175" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0284c7">n_ext = e_r</text>

  <line x1="420" y1="180" x2="520" y2="180" stroke="#dc2626" stroke-width="2.5" marker-end="url(#g-arr)"/>
  <text x="525" y="195" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">E(r) e_r</text>

  <!-- Radius r and Height h -->
  <line x1="300" y1="180" x2="420" y2="180" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="350" y="173" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#475569">rayon r</text>

  <line x1="160" y1="110" x2="160" y2="250" stroke="#475569" stroke-width="1.5"/>
  <line x1="155" y1="110" x2="165" y2="110" stroke="#475569" stroke-width="1.5"/>
  <line x1="155" y1="250" x2="165" y2="250" stroke="#475569" stroke-width="1.5"/>
  <text x="145" y="185" text-anchor="end" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#475569">hauteur h</text>

  <!-- Key formula box -->
  <rect x="20" y="40" width="140" height="90" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="30" y="60" font-family="Times New Roman, serif" font-size="12" font-weight="bold" fill="#0f172a">Flux Total :</text>
  <text x="30" y="78" font-family="Times New Roman, serif" font-size="12" fill="#334155">Φ = E(r) · (2π r h)</text>
  <text x="30" y="98" font-family="Times New Roman, serif" font-size="12" font-weight="bold" fill="#0f172a">Gauss :</text>
  <text x="30" y="116" font-family="Times New Roman, serif" font-size="12" fill="#334155">Φ = Q_int / ε₀</text>
</svg>'''
    return svg

def create_svg_em_wave():
    # 3D EM Wave showing E, B, k vectors
    svg = '''<svg width="600" height="340" viewBox="0 0 600 340" xmlns="http://www.w3.org/2000/svg" style="background:#fcfcfd; border:1px solid #d0d7de; border-radius:8px; margin:15px auto; display:block;">
  <defs>
    <marker id="w-k" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <marker id="w-e" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#2563eb"/>
    </marker>
    <marker id="w-b" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
  </defs>

  <text x="300" y="26" text-anchor="middle" font-family="Times New Roman, serif" font-size="17" font-weight="bold" fill="#0f172a">Onde Électromagnétique Plane Harmonique 3D : Trièdre Direct (E, B, k)</text>

  <!-- Propagation Axis z -->
  <line x1="50" y1="180" x2="550" y2="180" stroke="#1e293b" stroke-width="2" marker-end="url(#w-k)"/>
  <text x="560" y="185" font-family="Times New Roman, serif" font-size="16" font-weight="bold" fill="#1e293b">z (propagation k)</text>

  <!-- Vertical Axis x (Electric Field E) -->
  <line x1="80" y1="290" x2="80" y2="60" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="75" y="50" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#2563eb">x (E)</text>

  <!-- Transverse Axis y (Magnetic Field B, isometric projection) -->
  <line x1="80" y1="180" x2="30" y2="240" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="20" y="255" font-family="Times New Roman, serif" font-size="15" font-weight="bold" fill="#dc2626">y (B)</text>

  <!-- Sinusoidal E field (vertical) and B field (in inclined plane) -->
  <!-- wavelength = 200px, 2 cycles from x=80 to x=480 -->
  <!-- Drawing arrows for E and B along the wave -->
  '''
    # generate wave lines
    e_path = "M 80,180 "
    b_path = "M 80,180 "
    points = []
    for z in range(80, 500, 5):
        phase = (z - 80) * (2 * math.pi / 200)
        # E is along vertical (y in svg is negative of E)
        amp_e = 60 * math.sin(phase)
        y_svg_e = 180 - amp_e
        e_path += f"L {z},{y_svg_e:.1f} "

        # B is along inclined axis (dx = -0.7 * amp_b, dy = 0.5 * amp_b)
        amp_b = 40 * math.sin(phase)
        bx = z - amp_b * 0.7
        by = 180 + amp_b * 0.5
        b_path += f"L {bx:.1f},{by:.1f} "

    svg += f'<path d="{e_path}" fill="none" stroke="#2563eb" stroke-width="2.5"/>\n'
    svg += f'<path d="{b_path}" fill="none" stroke="#dc2626" stroke-width="2.5"/>\n'

    # Add sampled vector arrows
    for z in [130, 180, 230, 330, 380, 430]:
        phase = (z - 80) * (2 * math.pi / 200)
        amp_e = 60 * math.sin(phase)
        if abs(amp_e) > 5:
            svg += f'<line x1="{z}" y1="180" x2="{z}" y2="{180-amp_e:.1f}" stroke="#2563eb" stroke-width="1.5" marker-end="url(#w-e)"/>\n'
        amp_b = 40 * math.sin(phase)
        if abs(amp_b) > 5:
            svg += f'<line x1="{z}" y1="180" x2="{z - amp_b*0.7:.1f}" y2="{180 + amp_b*0.5:.1f}" stroke="#dc2626" stroke-width="1.5" marker-end="url(#w-b)"/>\n'

    # Wavelength label
    svg += '''
  <line x1="130" y1="110" x2="330" y2="110" stroke="#475569" stroke-width="1.5"/>
  <line x1="130" y1="105" x2="130" y2="115" stroke="#475569" stroke-width="1.5"/>
  <line x1="330" y1="105" x2="330" y2="115" stroke="#475569" stroke-width="1.5"/>
  <text x="230" y="103" text-anchor="middle" font-family="Times New Roman, serif" font-size="14" font-weight="bold" fill="#0f172a">Longueur d'onde λ = c / f</text>

  <!-- Poynting vector Pi -->
  <rect x="420" y="45" width="165" height="85" rx="5" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="430" y="65" font-family="Times New Roman, serif" font-size="12" font-weight="bold" fill="#0f172a">Vecteur de Poynting :</text>
  <text x="430" y="83" font-family="Times New Roman, serif" font-size="12" fill="#2563eb">• Π = (E ∧ B) / μ₀</text>
  <text x="430" y="101" font-family="Times New Roman, serif" font-size="12" fill="#dc2626">• B₀ = E₀ / c</text>
  <text x="430" y="119" font-family="Times New Roman, serif" font-size="12" fill="#334155">• E ⟂ B ⟂ k (Onde transverse)</text>
</svg>'''
    return svg

with open('src_book/fig_cartesian.svg', 'w') as f:
    f.write(create_svg_cartesian())
with open('src_book/fig_cylindrical.svg', 'w') as f:
    f.write(create_svg_cylindrical())
with open('src_book/fig_spherical.svg', 'w') as f:
    f.write(create_svg_spherical())
with open('src_book/fig_symmetry.svg', 'w') as f:
    f.write(create_svg_symmetry())
with open('src_book/fig_gauss_cylinder.svg', 'w') as f:
    f.write(create_svg_gauss_cylinder())
with open('src_book/fig_em_wave.svg', 'w') as f:
    f.write(create_svg_em_wave())

print("All 3D SVGs successfully generated!")
