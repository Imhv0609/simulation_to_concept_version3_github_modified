#!/usr/bin/env python3
"""
Inject AndroidBridge student-interaction reporting into simulation HTML files.
Appends a <script> block before </body> in each file.
Idempotent: skips files that already have the bridge snippet.
"""

import os
import re

BASE = "/Users/imhvs0609/Desktop/Personal Education/simulation_to_concept_version3_github_modified"

BRIDGE_MARKER = "AndroidBridge: student interaction"

SCRIPT_TEMPLATE = """
<script>
/* {marker} */
(function () {{
    var SKIP = ['help','hint','next','submit','reset','close','back','check','nxt','cancel'];
    function skip(el) {{
        if (!el) return false;
        var t = (el.textContent||'').toLowerCase().trim().slice(0,20);
        var i = (el.id||'').toLowerCase();
        var c = (el.className||'').toLowerCase();
        return SKIP.some(function(w){{ return t===w||i.indexOf(w)!==−1||c.indexOf(w)!==−1; }});
    }}
    function payload() {{
        try {{ return ({payload_expr}); }}
        catch(e) {{ return {{initialState:'changed'}}; }}
    }}
    function report() {{
        if (!window.AndroidBridge) return;
        try {{ window.AndroidBridge.onParamChanged(JSON.stringify(payload())); }} catch(e) {{}}
    }}
    {extra_setup}
    document.addEventListener('click', function(e) {{
        var el = e.target;
        while (el && el !== document.body) {{
            if (el.tagName==='BUTTON' || el.hasAttribute('onclick') ||
                (el.dataset && (el.dataset.m||el.dataset.i||el.dataset.v||el.dataset.state))) {{
                if (!skip(el)) setTimeout(report, 130);
                break;
            }}
            el = el.parentElement;
        }}
    }}, true);
    document.addEventListener('input', function(e) {{
        if (e.target.type==='range') setTimeout(report, 130);
    }}, true);
}})();
</script>
"""

# (directory, filename, payload_js_expr, extra_setup_js)
# extra_setup_js: optional JS to run once after page load (e.g. function wrappers)
MANIFEST = [
    # ── SCIENCE CHAPTER 2 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter2_simulation1_hidden_message_kn.html",
     "typeof sprayCount!=='undefined'?{initialState:sprayCount>0?'revealing':'hidden'}:{initialState:'hidden'}",""),

    ("simulations_kannada","science_chapter2_simulation2_litmus_indicator_kn.html",
     "typeof state!=='undefined'&&state&&state.solution?{initialState:state.solution}:{initialState:'neutral'}",""),

    ("simulations_kannada","science_chapter2_simulation3_properties_acids_bases_kn.html",
     "{initialState:(typeof selectedPanel!=='undefined'?selectedPanel:'acids')+(typeof selectedSubstance!=='undefined'?'_'+selectedSubstance:'')}",""),

    ("simulations_kannada","science_chapter2_simulation4_red_rose_indicator_kn.html",
     "typeof state!=='undefined'&&state&&state.solution?{initialState:state.solution}:{initialState:'neutral'}",""),

    ("simulations_kannada","science_chapter2_simulation5_turmeric_indicator_kn.html",
     "typeof state!=='undefined'&&state&&state.solution?{initialState:state.solution}:{initialState:'neutral'}",""),

    ("simulations_kannada","science_chapter2_simulation6_olfactory_indicator_kn.html",
     "typeof state!=='undefined'&&state&&state.solution?{initialState:state.solution}:{initialState:'acidic'}",""),

    ("simulations_kannada","science_chapter2_simulation7_neutralisation_reaction_kn.html",
     "typeof baseAmount!=='undefined'?{initialState:baseAmount<40?'acidic':baseAmount>60?'basic':'neutral'}:{initialState:'neutral'}",""),

    ("simulations_kannada","science_chapter2_simulation8_ant_bite_treatment_kn.html",
     "typeof state!=='undefined'&&typeof state==='string'?{initialState:state}:{initialState:'normal'}",""),

    ("simulations_kannada","science_chapter2_simulation9_soil_treatment_kn.html",
     "typeof selectedSoilType!=='undefined'?{initialState:selectedSoilType}:{initialState:'neutral'}",""),

    ("simulations_kannada","science_chapter2_simulation10_industrial_waste_treatment_kn.html",
     "typeof state!=='undefined'&&typeof state==='string'?{initialState:state}:{initialState:'initial'}",""),

    # ── SCIENCE CHAPTER 3 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter3_simulation1_electricity_uses_kn.html",
     "typeof selectedCategory!=='undefined'?{initialState:selectedCategory}:{initialState:'all'}",""),

    ("simulations_kannada","science_chapter3_simulation2_electricity_sources_kn.html",
     "window._src?{initialState:window._src}:{initialState:'hydro'}",
     "if(typeof showSource==='function'){var _os=showSource;window.showSource=function(t){window._src=t;return _os.apply(this,arguments);};}"),

    ("simulations_kannada","science_chapter3_simulation3_torch_components_kn.html",
     "{initialState:(typeof currentMode!=='undefined'?currentMode:'assembled')+(typeof isOn!=='undefined'&&isOn?'_on':'_off')}",""),

    ("simulations_kannada","science_chapter3_simulation4_electric_cell_kn.html",
     "typeof selectedTerminal!=='undefined'?{initialState:selectedTerminal}:{initialState:'positive'}",""),

    ("simulations_kannada","science_chapter3_simulation5_battery_connection_kn.html",
     "typeof selectedConfig!=='undefined'?{initialState:selectedConfig}:(typeof connectionMode!=='undefined'?{initialState:connectionMode}:{initialState:'series'})",""),

    ("simulations_kannada","science_chapter3_simulation6_lamp_types_kn.html",
     "typeof selectedLampType!=='undefined'?{initialState:selectedLampType}:{initialState:'led'}",""),

    ("simulations_kannada","science_chapter3_simulation7_simple_circuit_kn.html",
     "typeof circuitComplete!=='undefined'?{initialState:circuitComplete?'complete':'incomplete'}:{initialState:'initial'}",""),

    ("simulations_kannada","science_chapter3_simulation8_electric_switch_kn.html",
     "typeof switchState!=='undefined'?{initialState:switchState}:(typeof isOn!=='undefined'?{initialState:isOn?'on':'off'}:{initialState:'off'})",""),

    ("simulations_kannada","science_chapter3_simulation9_circuit_symbols_kn.html",
     "typeof selectedSymbol!=='undefined'?{initialState:selectedSymbol}:{initialState:'battery'}",""),

    ("simulations_kannada","science_chapter3_simulation10_conductors_insulators_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'copper'}",""),

    # ── SCIENCE CHAPTER 4 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter4_simulation1_malleability_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'iron'}",""),

    ("simulations_kannada","science_chapter4_simulation2_ductility_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'copper'}",""),

    ("simulations_kannada","science_chapter4_simulation3_sonority_kn.html",
     "typeof selectedObject!=='undefined'?{initialState:selectedObject}:(typeof objectIcon!=='undefined'?{initialState:objectIcon}:{initialState:'metal'})",""),

    ("simulations_kannada","science_chapter4_simulation4_heat_conduction_kn.html",
     "typeof experimentRunning!=='undefined'?{initialState:experimentRunning?'running':'stopped'}:{initialState:'stopped'}",""),

    ("simulations_kannada","science_chapter4_simulation5_electrical_conductivity_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'copper'}",""),

    ("simulations_kannada","science_chapter4_simulation6_rusting_experiment_kn.html",
     "typeof days!=='undefined'?{initialState:String(days)}:{initialState:'1'}",""),

    ("simulations_kannada","science_chapter4_simulation7_metal_oxide_reaction_kn.html",
     "typeof step!=='undefined'?{initialState:String(step)}:{initialState:'0'}",""),

    ("simulations_kannada","science_chapter4_simulation8_nonmetal_oxide_reaction_kn.html",
     "typeof step!=='undefined'?{initialState:String(step)}:{initialState:'0'}",""),

    ("simulations_kannada","science_chapter4_simulation9_metals_nonmetals_compare_kn.html",
     "typeof currentProperty!=='undefined'?{initialState:currentProperty}:{initialState:'lustre'}",""),

    ("simulations_kannada","science_chapter4_simulation10_applications_kn.html",
     "typeof selectedCategory!=='undefined'?{initialState:selectedCategory}:{initialState:'metals'}",""),

    # ── SCIENCE CHAPTER 5 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter5_simulation1_physical_changes_kn.html",
     "typeof currentExample!=='undefined'?{initialState:currentExample}:{initialState:'paper'}",""),

    ("simulations_kannada","science_chapter5_simulation2_chemical_changes_kn.html",
     "typeof currentExperiment!=='undefined'?{initialState:currentExperiment}:{initialState:'vinegar'}",""),

    # sim3 reversible_irreversible: Type C (quiz) - SKIPPED

    ("simulations_kannada","science_chapter5_simulation4_states_of_matter_kn.html",
     "typeof temp!=='undefined'?{initialState:temp<0?'solid':temp<100?'liquid':'gas'}:{initialState:'liquid'}",""),

    ("simulations_kannada","science_chapter5_simulation5_fire_triangle_kn.html",
     "typeof elements!=='undefined'?{initialState:JSON.stringify(elements)}:{initialState:'initial'}",""),

    ("simulations_kannada","science_chapter5_simulation6_oxygen_combustion_kn.html",
     "typeof candleLit!=='undefined'?{initialState:candleLit&&typeof jarCovered!=='undefined'&&jarCovered?'covered':candleLit?'lit':'initial'}:{initialState:'initial'}",""),

    ("simulations_kannada","science_chapter5_simulation7_candle_burning_kn.html",
     "typeof currentMode!=='undefined'?{initialState:currentMode+(typeof candleLit!=='undefined'&&candleLit?'_lit':'')}:{initialState:'physical'}",""),

    ("simulations_kannada","science_chapter5_simulation8_combustion_examples_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'wood'}",""),

    # sim9 desirable_undesirable: Type C (quiz) - SKIPPED

    ("simulations_kannada","science_chapter5_simulation10_weathering_erosion_kn.html",
     "{initialState:typeof currentMode!=='undefined'?currentMode:'weathering',timeLevel:typeof timeLevel!=='undefined'?timeLevel:0}",""),

    # ── SCIENCE CHAPTER 6 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter6_simulation1_life_stages_kn.html",
     "typeof selectedStageIndex!=='undefined'?{initialState:String(selectedStageIndex)}:{initialState:'0'}",""),

    ("simulations_kannada","science_chapter6_simulation2_growth_chart_kn.html",
     "{initialState:typeof selectedGender!=='undefined'?selectedGender:'boy',age:typeof currentAge!=='undefined'?currentAge:12}",""),

    ("simulations_kannada","science_chapter6_simulation3_physical_changes_kn.html",
     "typeof currentChangeType!=='undefined'?{initialState:currentChangeType}:{initialState:'height'}",""),

    ("simulations_kannada","science_chapter6_simulation4_voice_changes_kn.html",
     "typeof age!=='undefined'?{initialState:String(age)}:{initialState:'12'}",""),

    ("simulations_kannada","science_chapter6_simulation5_menstrual_cycle_kn.html",
     "typeof currentDay!=='undefined'?{initialState:String(currentDay)}:{initialState:'1'}",""),

    ("simulations_kannada","science_chapter6_simulation6_emotional_changes_kn.html",
     "typeof selectedEmotion!=='undefined'?{initialState:selectedEmotion}:{initialState:'happy'}",""),

    ("simulations_kannada","science_chapter6_simulation7_nutrition_kn.html",
     "typeof selectedFoodGroup!=='undefined'?{initialState:selectedFoodGroup}:{initialState:'proteins'}",""),

    ("simulations_kannada","science_chapter6_simulation8_hygiene_kn.html",
     "typeof selectedPractice!=='undefined'?{initialState:selectedPractice}:{initialState:'bathing'}",""),

    ("simulations_kannada","science_chapter6_simulation9_healthy_habits_kn.html",
     "typeof selectedHabit!=='undefined'?{initialState:selectedHabit}:{initialState:'exercise'}",""),

    # sim10 say_no: Type C (scenario responses) - SKIPPED

    # ── SCIENCE CHAPTER 7 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter7_simulation1_heat_sources_kn.html",
     "typeof selectedRegion!=='undefined'?{initialState:selectedRegion}:(typeof selectedLocation!=='undefined'?{initialState:selectedLocation}:{initialState:'solar'})",""),

    ("simulations_kannada","science_chapter7_simulation2_conduction_kn.html",
     "typeof selectedMaterial!=='undefined'?{initialState:selectedMaterial}:{initialState:'metal'}",""),

    # sim3 conductors_insulators: Type C (classification quiz) - SKIPPED

    ("simulations_kannada","science_chapter7_simulation4_convection_kn.html",
     "typeof selectedFluid!=='undefined'?{initialState:selectedFluid+(typeof heatOn!=='undefined'&&heatOn?'_heated':'')}:{initialState:'water'}",""),

    ("simulations_kannada","science_chapter7_simulation5_land_sea_breeze_kn.html",
     "{initialState:typeof selectedSeason!=='undefined'?selectedSeason:'summer',timeOfDay:typeof timeOfDay!=='undefined'?timeOfDay:12}",""),

    ("simulations_kannada","science_chapter7_simulation6_radiation_kn.html",
     "typeof selectedSurface!=='undefined'?{initialState:selectedSurface}:{initialState:'light'}",""),

    ("simulations_kannada","science_chapter7_simulation7_combined_heat_transfer_kn.html",
     "typeof currentTransferType!=='undefined'?{initialState:currentTransferType}:{initialState:'conduction'}",""),

    ("simulations_kannada","science_chapter7_simulation8_water_cycle_kn.html",
     "typeof currentStage!=='undefined'?{initialState:currentStage}:{initialState:'evaporation'}",""),

    ("simulations_kannada","science_chapter7_simulation9_infiltration_kn.html",
     "typeof selectedSoilType!=='undefined'?{initialState:selectedSoilType}:{initialState:'clay'}",""),

    ("simulations_kannada","science_chapter7_simulation10_water_conservation_kn.html",
     "typeof selectedMethod!=='undefined'?{initialState:selectedMethod}:{initialState:'rainwater'}",""),

    # ── SCIENCE CHAPTER 8 ──────────────────────────────────────────────
    ("simulations_kannada","science_chapter8_simulation1_historical_clocks_kn.html",
     "typeof selectedClockIndex!=='undefined'?{initialState:String(selectedClockIndex)}:{initialState:'0'}",""),

    ("simulations_kannada","science_chapter8_simulation2_sundial_kn.html",
     "typeof hours!=='undefined'?{hour:hours}:(typeof currentHour!=='undefined'?{hour:currentHour}:{hour:12})",""),

    ("simulations_kannada","science_chapter8_simulation3_pendulum_kn.html",
     "{initialState:'adjusted',pendulumLength:typeof pendulumLength!=='undefined'?pendulumLength:5,swingAmplitude:typeof swingAmplitude!=='undefined'?swingAmplitude:30}",""),

    ("simulations_kannada","science_chapter8_simulation4_pendulum_timing_kn.html",
     "typeof currentPendulum!=='undefined'?{initialState:currentPendulum}:{initialState:'medium'}",""),

    ("simulations_kannada","science_chapter8_simulation5_time_units_kn.html",
     "typeof selectedUnit!=='undefined'?{value:selectedUnit}:{value:'second'}",""),

    ("simulations_kannada","science_chapter8_simulation6_speed_calculator_kn.html",
     "{initialState:'adjusted',distance:typeof distance!=='undefined'?distance:10,time:typeof time!=='undefined'?time:2}",""),

    ("simulations_kannada","science_chapter8_simulation7_speed_race_kn.html",
     "typeof selectedSpeed!=='undefined'?{initialState:String(selectedSpeed)}:{initialState:'5'}",""),

    ("simulations_kannada","science_chapter8_simulation8_uniform_motion_kn.html",
     "{initialState:'adjusted',speed:typeof speed!=='undefined'?speed:5,time:typeof time!=='undefined'?time:2}",""),

    ("simulations_kannada","science_chapter8_simulation9_nonuniform_motion_kn.html",
     "{initialState:'adjusted',acceleration:typeof acceleration!=='undefined'?acceleration:2,time:typeof time!=='undefined'?time:2}",""),

    ("simulations_kannada","science_chapter8_simulation10_speedometer_kn.html",
     "typeof currentSpeed!=='undefined'?{initialState:String(Math.round(currentSpeed))}:{initialState:'0'}",""),

    # ── MATHS SIMULATIONS ──────────────────────────────────────────────
    ("maths_simulations_kannada","math_chapter1_simulation1_place_value_calculator_kn.html",
     "typeof currentMode!=='undefined'?{mode:currentMode}:{mode:'explore'}",""),

    ("maths_simulations_kannada","math_chapter1_simulation2_number_systems_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'explore',number:typeof currentNum!=='undefined'?currentNum:100}",""),

    ("maths_simulations_kannada","math_chapter1_simulation3_sense_of_scale_kn.html",
     "typeof scIdx!=='undefined'?{scenario:scIdx}:{scenario:0}",""),

    ("maths_simulations_kannada","math_chapter1_simulation4_rounding_estimation_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'explore',number:typeof currentNum!=='undefined'?currentNum:12345}",""),

    ("maths_simulations_kannada","math_chapter1_simulation5_multiplication_patterns_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'explore',multiplier:typeof currentMultiplier!=='undefined'?currentMultiplier:2}",""),

    ("maths_simulations_kannada","math_chapter2_simulation1_expression_evaluator_kn.html",
     "typeof pIdx!=='undefined'?{problem:pIdx}:{problem:0}",""),

    ("maths_simulations_kannada","math_chapter2_simulation2_brackets_signs_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'learn',problemIndex:typeof pIdx!=='undefined'?pIdx:0}",""),

    ("maths_simulations_kannada","math_chapter2_simulation3_distributive_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'learn',problemIndex:typeof pIdx!=='undefined'?pIdx:(typeof problemIndex!=='undefined'?problemIndex:0)}",""),

    # math_chapter2_simulation4_expression_compare: Type C (quiz buttons < = >) - SKIPPED

    ("maths_simulations_kannada","math_chapter2_simulation5_expression_engineer_kn.html",
     "typeof challenge!=='undefined'?{challenge:challenge}:(typeof targetValue!=='undefined'?{challenge:String(targetValue)}:{challenge:'easy'})",""),

    ("maths_simulations_kannada","math_chapter3_simulation1_decimal_number_line_kn.html",
     "{mode:typeof mode!=='undefined'?mode:'explore',number:typeof currentNumber!=='undefined'?currentNumber:0.5}",""),
]


def inject(filepath, payload_expr, extra_setup, marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if marker in content:
        print(f"  SKIP (already has bridge): {os.path.basename(filepath)}")
        return False

    if '</body>' not in content.lower():
        print(f"  WARN (no </body> found):   {os.path.basename(filepath)}")
        return False

    extra_js = f"\n    {extra_setup}" if extra_setup.strip() else ""

    snippet = SCRIPT_TEMPLATE.format(
        marker=marker,
        payload_expr=payload_expr,
        extra_setup=extra_js
    )

    # Replace last occurrence of </body> (case-insensitive)
    pattern = re.compile(r'</body>', re.IGNORECASE)
    parts = pattern.split(content)
    if len(parts) < 2:
        print(f"  WARN (split failed):       {os.path.basename(filepath)}")
        return False

    new_content = '</body>'.join(parts[:-1]) + snippet + '</body>' + parts[-1]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  OK:                        {os.path.basename(filepath)}")
    return True


def main():
    ok = 0
    skipped = 0
    errors = 0

    for (subdir, filename, payload_expr, extra_setup) in MANIFEST:
        filepath = os.path.join(BASE, subdir, filename)
        if not os.path.exists(filepath):
            print(f"  MISSING:                   {filename}")
            errors += 1
            continue
        result = inject(filepath, payload_expr, extra_setup, BRIDGE_MARKER)
        if result:
            ok += 1
        else:
            skipped += 1

    print(f"\n{'='*50}")
    print(f"Done. Injected: {ok}  |  Skipped: {skipped}  |  Errors: {errors}")


if __name__ == '__main__':
    main()
